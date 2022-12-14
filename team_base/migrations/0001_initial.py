# Generated by Django 4.0.4 on 2022-10-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamBase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=64, unique=True)),
                ('description', models.CharField(default='', max_length=64)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('admin', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
