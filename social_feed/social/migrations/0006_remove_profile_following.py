# Generated by Django 4.0.2 on 2022-04-27 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_profile_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
    ]
