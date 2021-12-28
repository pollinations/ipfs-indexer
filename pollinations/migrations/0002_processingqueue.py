# Generated by Django 4.0 on 2021-12-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pollinations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProcessingQueue",
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
                ("processed_at", models.DateTimeField()),
            ],
        ),
    ]
