# Generated by Django 3.2.13 on 2022-07-31 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20220730_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutmovie',
            name='date',
        ),
        migrations.RemoveField(
            model_name='movieimg',
            name='date',
        ),
    ]