from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .models import Profile


# ── Profile auto-creation ────────────────────────────────────────────────────

@receiver(post_save, sender=User)
def create_person(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name=instance.first_name)


@receiver(post_save, sender=User)
def save_person(sender, instance, **kwargs):
    instance.profile.save()


# ── Study subjects: migrate a guest's session choice to their profile ────────

@receiver(user_logged_in)
def migrate_study_subjects(sender, request, user, **kwargs):
    raw = request.session.pop('study_subjects', None)
    if raw and not user.profile.study_subjects:
        user.profile.study_subjects = raw
        user.profile.save(update_fields=['study_subjects'])


# ── Helpers ──────────────────────────────────────────────────────────────────

def _bulk_notify(users_qs, notif_type, title, message, url):
    from .models import Notification
    notifs = [
        Notification(user=u, notif_type=notif_type, title=title, message=message, url=url)
        for u in users_qs
    ]
    Notification.objects.bulk_create(notifs, ignore_conflicts=True)


# ── Homework assignment ──────────────────────────────────────────────────────

@receiver(post_save, sender='homework.HomeworkAssignment')
def notify_homework_assigned(sender, instance, created, **kwargs):
    if not created:
        return
    from .models import Notification
    hw = instance.homework
    Notification.objects.create(
        user=instance.panda.profile.user,
        notif_type=Notification.TYPE_HOMEWORK,
        title=str(_('New Homework: %(title)s') % {'title': hw.title}),
        message=str(_('%(master)s assigned you new homework.') % {'master': hw.master.name}),
        url=reverse('my_homework'),
    )


# ── Practice published ───────────────────────────────────────────────────────

@receiver(pre_save, sender='practice.Practice')
def practice_pre_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._old_published = sender.objects.get(pk=instance.pk).is_published
        except sender.DoesNotExist:
            instance._old_published = False
    else:
        instance._old_published = False


@receiver(post_save, sender='practice.Practice')
def notify_practice_published(sender, instance, created, **kwargs):
    old = getattr(instance, '_old_published', False)
    if not (instance.is_published and (created or not old)):
        return
    from .models import Notification
    users = User.objects.filter(profile__panda__masters=instance.master).distinct()
    _bulk_notify(
        users,
        Notification.TYPE_PRACTICE,
        str(_('New Practice: %(title)s') % {'title': instance.title}),
        str(_('%(master)s published a new practice.') % {'master': instance.master.name}),
        reverse('practice_detail', args=[instance.pk]),
    )


# ── Tutorial published ───────────────────────────────────────────────────────

@receiver(pre_save, sender='tutorial.Tutorial')
def tutorial_pre_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._old_published = sender.objects.get(pk=instance.pk).is_published
        except sender.DoesNotExist:
            instance._old_published = False
    else:
        instance._old_published = False


@receiver(post_save, sender='tutorial.Tutorial')
def notify_tutorial_published(sender, instance, created, **kwargs):
    old = getattr(instance, '_old_published', False)
    if not (instance.is_published and (created or not old)):
        return
    master = getattr(getattr(instance.author, 'profile', None), 'master', None)
    if not master:
        return
    from .models import Notification
    users = User.objects.filter(profile__panda__masters=master).distinct()
    _bulk_notify(
        users,
        Notification.TYPE_TUTORIAL,
        str(_('New Tutorial: %(title)s') % {'title': instance.title}),
        str(_('%(master)s published a new tutorial.') % {'master': master.name}),
        reverse('tutorial_detail', args=[instance.pk]),
    )


# ── Lesson published ─────────────────────────────────────────────────────────

@receiver(pre_save, sender='classroom.Lesson')
def lesson_pre_save(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._old_published = sender.objects.get(pk=instance.pk).is_published
        except sender.DoesNotExist:
            instance._old_published = False
    else:
        instance._old_published = False


@receiver(post_save, sender='classroom.Lesson')
def notify_lesson_published(sender, instance, created, **kwargs):
    old = getattr(instance, '_old_published', False)
    if not (instance.is_published and (created or not old)):
        return
    from .models import Notification
    classroom = instance.classroom
    pandas = classroom.get_all_pandas()
    users = User.objects.filter(profile__panda__in=pandas).distinct()
    _bulk_notify(
        users,
        Notification.TYPE_LESSON,
        str(_('New Lesson: %(lesson)s') % {'lesson': instance.title}),
        str(_('A new lesson was published in %(classroom)s.') % {'classroom': classroom.name}),
        reverse('classroom:lesson_detail', args=[classroom.pk, instance.pk]),
    )


# ── Classroom discussion created by master ───────────────────────────────────

@receiver(post_save, sender='classroom.ClassroomDiscussion')
def notify_classroom_discussion(sender, instance, created, **kwargs):
    if not created:
        return
    classroom = instance.classroom
    master_user = classroom.master.profile.user
    if instance.author != master_user:
        return
    from .models import Notification
    pandas = classroom.get_all_pandas()
    users = User.objects.filter(profile__panda__in=pandas).distinct().exclude(pk=master_user.pk)
    _bulk_notify(
        users,
        Notification.TYPE_DISCUSSION,
        str(_('New Discussion: %(title)s') % {'title': instance.title}),
        str(_('%(master)s started a new discussion in %(classroom)s.') % {
            'master': classroom.master.name,
            'classroom': classroom.name,
        }),
        reverse('classroom:discussion_thread', args=[classroom.pk, instance.pk]),
    )
