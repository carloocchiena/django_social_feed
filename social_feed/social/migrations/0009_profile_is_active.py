# Generated by Django 4.0.2 on 2022-05-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0008_alter_post_options_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
