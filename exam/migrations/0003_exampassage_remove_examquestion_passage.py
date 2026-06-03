from django.db import migrations, models
import django.db.models.deletion


def move_passages_forward(apps, schema_editor):
    ExamQuestion = apps.get_model('exam', 'ExamQuestion')
    ExamPassage = apps.get_model('exam', 'ExamPassage')
    for q in ExamQuestion.objects.exclude(passage=''):
        ExamPassage.objects.create(
            exam=q.exam,
            section=q.section,
            question_from=q.number,
            question_to=q.number,
            text=q.passage,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_alter_exam_options_alter_examchoice_options_and_more'),
    ]

    operations = [
        # 1. Create ExamPassage table
        migrations.CreateModel(
            name='ExamPassage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('listening', 'Listening / 듣기'), ('reading', 'Reading / 읽기'), ('writing', 'Writing / 쓰기')], max_length=20)),
                ('question_from', models.IntegerField()),
                ('question_to', models.IntegerField()),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='exam_images/')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passages', to='exam.exam')),
            ],
            options={'ordering': ['question_from']},
        ),
        # 2. Copy existing per-question passages into ExamPassage
        migrations.RunPython(move_passages_forward, migrations.RunPython.noop),
        # 3. Allow question_text to be blank
        migrations.AlterField(
            model_name='examquestion',
            name='question_text',
            field=models.TextField(blank=True),
        ),
        # 4. Remove passage fields from ExamQuestion
        migrations.RemoveField(model_name='examquestion', name='passage'),
        migrations.RemoveField(model_name='examquestion', name='passage_image'),
    ]
