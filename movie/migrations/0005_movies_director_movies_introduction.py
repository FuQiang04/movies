# Generated by Django 4.2.13 on 2024-06-11 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_movies_options_movies_href'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='director',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='introduction',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
