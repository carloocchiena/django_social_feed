# Generated by Django 4.0.2 on 2022-06-01 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_profile_coin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='coin',
            new_name='coins',
        ),
    ]