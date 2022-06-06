# Generated by Django 4.0.2 on 2022-06-03 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0013_post_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='coins',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='user_coins', to=settings.AUTH_USER_MODEL),
        ),
    ]
