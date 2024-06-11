# Generated by Django 4.2.13 on 2024-06-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movies_director_movies_introduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='China_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('href', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'China_movies',
                'verbose_name_plural': 'China_movies',
            },
        ),
        migrations.CreateModel(
            name='Janpa_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('href', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Janpa_movies',
                'verbose_name_plural': 'Janpa_movies',
            },
        ),
        migrations.CreateModel(
            name='new_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('href', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'new_movies',
                'verbose_name_plural': 'new_movies',
            },
        ),
        migrations.CreateModel(
            name='recommend_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('href', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'recommend_movies',
                'verbose_name_plural': 'recommend_movies',
            },
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='America_movies',
        ),
        migrations.AlterModelOptions(
            name='america_movies',
            options={'verbose_name': 'America_movies', 'verbose_name_plural': 'America_movies'},
        ),
    ]
