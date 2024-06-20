# Generated by Django 4.2.13 on 2024-06-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_delete_movies_alter_new_movies_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new_movies',
            options={'verbose_name': 'new_movies', 'verbose_name_plural': 'new_movies'},
        ),
        migrations.RenameField(
            model_name='america_movies',
            old_name='introduction',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='china_movies',
            old_name='introduction',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='janpa_movies',
            old_name='introduction',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='recommend_movies',
            old_name='introduction',
            new_name='img',
        ),
        migrations.RemoveField(
            model_name='america_movies',
            name='director',
        ),
        migrations.RemoveField(
            model_name='america_movies',
            name='time',
        ),
        migrations.RemoveField(
            model_name='china_movies',
            name='director',
        ),
        migrations.RemoveField(
            model_name='china_movies',
            name='time',
        ),
        migrations.RemoveField(
            model_name='janpa_movies',
            name='director',
        ),
        migrations.RemoveField(
            model_name='janpa_movies',
            name='time',
        ),
        migrations.RemoveField(
            model_name='recommend_movies',
            name='director',
        ),
        migrations.RemoveField(
            model_name='recommend_movies',
            name='time',
        ),
        migrations.AddField(
            model_name='america_movies',
            name='actor',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='china_movies',
            name='actor',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='janpa_movies',
            name='actor',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommend_movies',
            name='actor',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='america_movies',
            name='href',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='china_movies',
            name='href',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='janpa_movies',
            name='href',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recommend_movies',
            name='href',
            field=models.CharField(max_length=200),
        ),
    ]