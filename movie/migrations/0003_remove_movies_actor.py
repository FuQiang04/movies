# Generated by Django 4.2.13 on 2024-06-11 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movies_actor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='actor',
        ),
    ]