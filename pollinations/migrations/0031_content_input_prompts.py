# Generated by Django 4.0 on 2021-12-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pollinations", "0030_content_input_city_content_input_country_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="content",
            name="input_prompts",
            field=models.TextField(null=True),
        ),
    ]
