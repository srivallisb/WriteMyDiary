# Generated by Django 3.0.5 on 2020-05-06 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diary', '0002_features_favourites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='features',
            name='favourites',
        ),
        migrations.AddField(
            model_name='features',
            name='favourites',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]
