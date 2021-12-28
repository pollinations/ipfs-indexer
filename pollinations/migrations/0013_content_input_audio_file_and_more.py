# Generated by Django 4.0 on 2021-12-28 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pollinations", "0012_content_input_models_content_input_speed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="input_audio_file",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="input_motion_randomness",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="input_motion_react",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="input_motion_react_to",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="input_pulse_react",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="input_pulse_react_to",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="content",
            name="input_truncation",
            field=models.TextField(null=True),
        ),
    ]
