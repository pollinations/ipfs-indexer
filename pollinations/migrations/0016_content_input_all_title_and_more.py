# Generated by Django 4.0 on 2021-12-28 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollinations', '0015_content_input_batch_size_content_input_prompt'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='input_all_title',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_choose_diffusion_model',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_cut_batches',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_cut_pow',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_cutn',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_imageHeight',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_imageWidth',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_init_weight_mse',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_resSize',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='input_starting_noise',
            field=models.TextField(null=True),
        ),
    ]