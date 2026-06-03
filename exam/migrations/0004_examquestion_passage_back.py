from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_exampassage_remove_examquestion_passage'),
    ]

    operations = [
        migrations.AddField(
            model_name='examquestion',
            name='passage',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examquestion',
            name='passage_image',
            field=models.ImageField(blank=True, null=True, upload_to='exam_images/'),
        ),
    ]
