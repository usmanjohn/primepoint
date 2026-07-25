"""Copy writing drills out of `corner` and into `examprep`.

Corner is the reading library; an exam-writing drill belongs with the exam it
prepares you for. The old model hung off a Corner subject ("Korean"), which
could not express whether a drill was TOPIK 쓰기 or IELTS Task 2 — the new one
hangs off an ExamTrack.

Copy-then-delete rather than a table rename, because the foreign key points at a
different table now. Words are rebuilt from the copied rows rather than re-parsed,
so a drill whose vocab was hand-corrected in admin keeps exactly what it had.
"""
from django.db import migrations

# Which exam track a Corner subject's drills belong to. Every drill that exists
# today is Korean/TOPIK; anything unmapped is reported and skipped rather than
# silently dropped into the wrong exam.
SUBJECT_TO_TRACK = {
    'korean': 'topik',
    'english': 'ielts',
}


def move_drills(apps, schema_editor):
    WritingPractice = apps.get_model('corner', 'WritingPractice')
    WritingDrill = apps.get_model('examprep', 'WritingDrill')
    WritingDrillWord = apps.get_model('examprep', 'WritingDrillWord')
    WritingDrillProgress = apps.get_model('examprep', 'WritingDrillProgress')
    ExamTrack = apps.get_model('examprep', 'ExamTrack')

    tracks = {t.slug: t for t in ExamTrack.objects.all()}
    moved = skipped = 0

    for old in WritingPractice.objects.select_related('subject').all():
        track_slug = SUBJECT_TO_TRACK.get(old.subject.slug)
        track = tracks.get(track_slug) if track_slug else None
        if track is None:
            print(f'  ! skipped "{old.title}" — no exam track for subject '
                  f'"{old.subject.slug}"')
            skipped += 1
            continue

        new = WritingDrill.objects.create(
            track=track,
            qtype=old.qtype,
            title=old.title,
            summary=old.summary,
            prompt=old.prompt,
            chart=old.chart,
            template_body=old.template_body,
            model_answer=old.model_answer,
            tips=old.tips,
            author_id=old.author_id,
            order=old.order,
            is_published=old.is_published,
            views=old.views,
        )
        WritingDrillWord.objects.bulk_create([
            WritingDrillWord(drill=new, word=w.word, translation=w.translation,
                             pos=w.pos, order=w.order)
            for w in old.words.all()
        ])
        WritingDrillProgress.objects.bulk_create([
            WritingDrillProgress(drill=new, user_id=p.user_id,
                                 points_awarded=p.points_awarded)
            for p in old.progress.all()
        ])
        moved += 1

    if moved or skipped:
        print(f'  moved {moved} writing drills into examprep'
              + (f', skipped {skipped}' if skipped else ''))


def unmove_drills(apps, schema_editor):
    """Reverse: put them back on the Corner subject they came from."""
    WritingPractice = apps.get_model('corner', 'WritingPractice')
    WritingPracticeWord = apps.get_model('corner', 'WritingPracticeWord')
    WritingPracticeProgress = apps.get_model('corner', 'WritingPracticeProgress')
    WritingDrill = apps.get_model('examprep', 'WritingDrill')
    Subject = apps.get_model('corner', 'Subject')

    track_to_subject = {v: k for k, v in SUBJECT_TO_TRACK.items()}
    subjects = {s.slug: s for s in Subject.objects.all()}

    for drill in WritingDrill.objects.select_related('track').all():
        subject = subjects.get(track_to_subject.get(drill.track.slug))
        if subject is None:
            continue
        old = WritingPractice.objects.create(
            subject=subject, qtype=drill.qtype, title=drill.title,
            summary=drill.summary, prompt=drill.prompt, chart=drill.chart,
            template_body=drill.template_body, model_answer=drill.model_answer,
            tips=drill.tips, author_id=drill.author_id, order=drill.order,
            is_published=drill.is_published, views=drill.views,
        )
        WritingPracticeWord.objects.bulk_create([
            WritingPracticeWord(practice=old, word=w.word, translation=w.translation,
                                pos=w.pos, order=w.order)
            for w in drill.words.all()
        ])
        WritingPracticeProgress.objects.bulk_create([
            WritingPracticeProgress(practice=old, user_id=p.user_id,
                                    points_awarded=p.points_awarded)
            for p in drill.progress.all()
        ])
    WritingDrill.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('examprep', '0006_writingdrill_writingdrillword_writingdrillprogress'),
        ('corner', '0006_story_image'),
    ]

    operations = [
        migrations.RunPython(move_drills, unmove_drills),
    ]
