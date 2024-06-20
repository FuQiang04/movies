# Generated by Django 4.2.13 on 2024-06-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_alter_movies_actor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='movies',
        ),
        migrations.AlterModelOptions(
            name='new_movies',
            options={'verbose_name': 'movies', 'verbose_name_plural': 'movies'},
        ),
        migrations.RenameField(
            model_name='new_movies',
            old_name='introduction',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='new_movies',
            name='director',
        ),
        migrations.RemoveField(
            model_name='new_movies',
            name='time',
        ),
        migrations.AddField(
            model_name='new_movies',
            name='actor',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new_movies',
            name='href',
            field=models.CharField(max_length=200),
        ),
    ]