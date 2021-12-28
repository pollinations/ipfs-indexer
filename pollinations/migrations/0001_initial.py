# Generated by Django 4.0 on 2021-12-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PollinationsCID",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cid", models.CharField(max_length=255)),
                ("raw_text_input", models.TextField()),
                ("tags", models.JSONField()),
                ("text_output", models.TextField()),
                ("notebook_name", models.TextField()),
            ],
        ),
    ]
