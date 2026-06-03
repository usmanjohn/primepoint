from django.db import migrations


def drop_if_exists(apps, schema_editor):
    """
    Migration 0004_examquestion_passage_back was applied in production but its
    file was later reverted, leaving 'passage' and 'passage_image' columns in
    the DB while the model no longer defines them.  Drop them safely.
    """
    vendor = schema_editor.connection.vendor
    if vendor == 'postgresql':
        schema_editor.execute(
            'ALTER TABLE exam_examquestion DROP COLUMN IF EXISTS passage'
        )
        schema_editor.execute(
            'ALTER TABLE exam_examquestion DROP COLUMN IF EXISTS passage_image'
        )
    else:
        with schema_editor.connection.cursor() as cursor:
            cursor.execute('PRAGMA table_info(exam_examquestion)')
            columns = {row[1] for row in cursor.fetchall()}
        if 'passage' in columns:
            schema_editor.execute(
                'ALTER TABLE exam_examquestion DROP COLUMN passage'
            )
        if 'passage_image' in columns:
            schema_editor.execute(
                'ALTER TABLE exam_examquestion DROP COLUMN passage_image'
            )


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_exampassage_remove_examquestion_passage'),
    ]

    operations = [
        migrations.RunPython(drop_if_exists, migrations.RunPython.noop),
    ]
