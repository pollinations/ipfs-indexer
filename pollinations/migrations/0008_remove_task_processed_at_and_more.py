# Generated by Django 4.0 on 2021-12-28 01:06

from django.db import migrations, models
import pollinations.models


class Migration(migrations.Migration):

    dependencies = [
        ('pollinations', '0007_task_delete_queue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='processed_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='processing_started_at',
        ),
        migrations.RemoveField(
            model_name='task',
            name='state',
        ),
        migrations.AddField(
            model_name='task',
            name='state_updates',
            field=models.JSONField(default=pollinations.models.empty_jsonb_array),
        ),
        migrations.AlterField(
            model_name='content',
            name='cid',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='cid',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]