# Generated by Django 5.2 on 2025-04-22 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
    ]
