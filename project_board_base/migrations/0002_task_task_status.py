# Generated by Django 4.0.4 on 2022-10-16 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_board_base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('OP', 'Open'), ('IP', 'In_Progress'), ('CP', 'Complete')], default='OP', max_length=2),
        ),
    ]
