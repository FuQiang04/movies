# Generated by Django 4.2.13 on 2024-06-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_remove_movies_actor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movies',
            options={'verbose_name': 'movies', 'verbose_name_plural': 'movies'},
        ),
        migrations.AddField(
            model_name='movies',
            name='href',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
