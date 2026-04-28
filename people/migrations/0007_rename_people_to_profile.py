from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0006_people_is_cofounder_people_is_director"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="People",
            new_name="Profile",
        ),
    ]
