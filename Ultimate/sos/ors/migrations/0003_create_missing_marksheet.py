
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ors', '0002_marksheet_student'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.CreateModel(
                    name='Marksheet',
                    fields=[
                        (
                            'id',
                            models.BigAutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name='ID',
                            ),
                        ),
                        ('roll_no', models.CharField(max_length=50)),
                        ('student_id', models.IntegerField()),
                        ('student_name', models.CharField(max_length=50)),
                        ('physics', models.IntegerField()),
                        ('chemistry', models.IntegerField()),
                        ('maths', models.IntegerField()),
                    ],
                    options={
                        'db_table': 'sos_marksheet',
                    },
                ),
            ],
            state_operations=[],
        ),
    ]
