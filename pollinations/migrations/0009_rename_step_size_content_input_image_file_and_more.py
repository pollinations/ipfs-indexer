# Generated by Django 4.0 on 2021-12-28 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollinations', '0008_remove_task_processed_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='step_size',
            new_name='input_image_file',
        ),
        migrations.AddField(
            model_name='content',
            name='input_step_size',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_text_input',
            field=models.TextField(null=True),
        ),
    ]