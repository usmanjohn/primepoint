"""Put the existing TOPIK mocks onto the new module machinery.

Before this migration a section was a bare string on the question row and the
three timings lived on the Exam. After it, every exam owns ExamModule rows and
the views read those instead — one code path for TOPIK and for the SAT.

Existing attempts are carried across too: the three `*_started_at` stamps and
the three `*_score` fields become ExamModuleAttempt rows, so a pupil who is
mid-exam when this deploys keeps their place and their clock.
"""
from django.db import migrations

TOPIK_MODULES = [
    # code, kind, label, label_uz, minutes-field, order
    ('listening', 'listening', 'Listening / 듣기', 'Tinglab tushunish', 'listening_minutes', 1),
    ('reading', 'reading', 'Reading / 읽기', 'Oʻqib tushunish', 'reading_minutes', 2),
    ('writing', 'writing', 'Writing / 쓰기', 'Yozish', 'writing_minutes', 3),
]


def seed(apps, schema_editor):
    Exam = apps.get_model('exam', 'Exam')
    ExamModule = apps.get_model('exam', 'ExamModule')
    ExamAttempt = apps.get_model('exam', 'ExamAttempt')
    ExamModuleAttempt = apps.get_model('exam', 'ExamModuleAttempt')
    ExamQuestion = apps.get_model('exam', 'ExamQuestion')

    for exam in Exam.objects.all():
        if exam.modules.exists():
            continue
        made = {}
        for code, kind, label, label_uz, minutes_field, order in TOPIK_MODULES:
            made[code] = ExamModule.objects.create(
                exam=exam, code=code, kind=kind, stage=1, difficulty='',
                label=label, label_uz=label_uz,
                minutes=getattr(exam, minutes_field, 60), order=order,
            )
        # Essay questions kept their old flag; give them the matching answer type.
        ExamQuestion.objects.filter(exam=exam, is_writing=True).update(answer_type='essay')

        for attempt in ExamAttempt.objects.filter(exam=exam):
            for code, _kind, _label, _uz, _mf, _order in TOPIK_MODULES:
                started = getattr(attempt, f'{code}_started_at', None)
                if not started:
                    continue
                total = ExamQuestion.objects.filter(exam=exam, section=code).count()
                percent = getattr(attempt, f'{code}_score', None)
                # The old score was a percentage; turn it back into a raw count so
                # the module row means the same thing for every exam format.
                raw = round(percent * total / 100) if (percent is not None and total) else None
                ExamModuleAttempt.objects.create(
                    attempt=attempt, module=made[code], started_at=started,
                    raw_score=raw, total_questions=total,
                )
            if attempt.current_section in made:
                attempt.current_module = made[attempt.current_section]
            attempt.status = 'completed' if attempt.current_section == 'completed' else 'in_progress'
            attempt.save(update_fields=['current_module', 'status'])


def unseed(apps, schema_editor):
    apps.get_model('exam', 'ExamModuleAttempt').objects.all().delete()
    apps.get_model('exam', 'ExamModule').objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [('exam', '0005_exam_exam_format_examattempt_break_until_and_more')]
    operations = [migrations.RunPython(seed, unseed)]
