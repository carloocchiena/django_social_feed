# Generated by Django 4.0.2 on 2022-06-03 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_alter_post_coins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='coins',
        ),
    ]
