# Generated by Django 3.0.5 on 2020-05-06 17:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0003_auto_20200506_2309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='favourites',
        ),
        migrations.AddField(
            model_name='features',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]
