def notification_context(request):
    if not request.user.is_authenticated:
        return {'unread_notif_count': 0}
    from .models import Notification
    count = Notification.objects.filter(user=request.user, is_read=False).count()
    return {'unread_notif_count': count}


def nav_counts(request):
    from django.core.cache import cache
    counts = cache.get('nav_counts_v3')
    if counts is None:
        from masters.models import Master
        from practice.models import Practice
        from panda.models import Panda
        from discussion.models import Thread
        from tutorial.models import Tutorial
        from classroom.models import Classroom
        from homework.models import Homework
        from exam.models import Exam
        from examprep.models import Lesson
        from corner.models import Story
        from games.views import GAME_COUNT
        counts = {
            'nav_masters_count': Master.objects.count(),
            'nav_practices_count': Practice.objects.filter(is_published=True).count(),
            'nav_students_count': Panda.objects.count(),
            'nav_threads_count': Thread.objects.count(),
            'nav_tutorials_count': Tutorial.objects.filter(is_published=True).count(),
            'nav_classrooms_count': Classroom.objects.filter(is_active=True).count(),
            'nav_homework_count': Homework.objects.count(),
            'nav_exams_count': Exam.objects.filter(is_published=True).count(),
            'nav_examprep_count': Lesson.objects.filter(is_published=True, track__is_published=True).count(),
            'nav_games_count': GAME_COUNT,
            'nav_corner_count': Story.objects.filter(
                is_published=True,
                collection__is_published=True,
                collection__subject__is_published=True,
            ).count(),
        }
        cache.set('nav_counts_v3', counts, 300)
    return counts
