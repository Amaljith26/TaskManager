# Generated by Django 5.2 on 2025-04-22 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_category_task_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
