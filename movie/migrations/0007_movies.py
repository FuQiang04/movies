# Generated by Django 4.2.13 on 2024-06-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_china_movies_janpa_movies_new_movies_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('href', models.CharField(max_length=50)),
                ('actor', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'movies',
                'verbose_name_plural': 'movies',
            },
        ),
    ]
