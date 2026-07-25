"""Drop the writing-drill tables — examprep owns them now.

Runs after `examprep.0007_move_writing_drills_from_corner`, which copies the
rows out; see the dependency below.

Hand-ordered: the autodetector emitted `RemoveField(practice)` before
`AlterUniqueTogether`, but `practice` is half of that unique constraint, so the
field cannot be dropped while the constraint still references it.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("corner", "0006_story_image"),
        # Must run AFTER the copy, or a fresh database would drop these tables
        # before examprep had read the drills out of them.
        ("examprep", "0007_move_writing_drills_from_corner"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="writingpracticeprogress",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="writingpracticeprogress",
            name="practice",
        ),
        migrations.RemoveField(
            model_name="writingpracticeprogress",
            name="user",
        ),
        migrations.RemoveField(
            model_name="writingpracticeword",
            name="practice",
        ),
        migrations.RemoveField(
            model_name="writingpractice",
            name="author",
        ),
        migrations.RemoveField(
            model_name="writingpractice",
            name="subject",
        ),
        migrations.DeleteModel(
            name="WritingPracticeProgress",
        ),
        migrations.DeleteModel(
            name="WritingPracticeWord",
        ),
        migrations.DeleteModel(
            name="WritingPractice",
        ),
    ]
