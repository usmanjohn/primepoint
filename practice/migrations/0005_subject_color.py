from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_practiceattempt_rating_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='color',
            field=models.CharField(default='#6366f1', help_text='Hex color for card accent, e.g. #6366f1', max_length=7),
        ),
    ]
