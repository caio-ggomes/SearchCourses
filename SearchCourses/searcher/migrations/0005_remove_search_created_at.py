# Generated by Django 3.1 on 2020-08-09 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searcher', '0004_remove_course_duration_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='created_at',
        ),
    ]
