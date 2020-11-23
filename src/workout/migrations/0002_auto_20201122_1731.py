# Generated by Django 3.1.2 on 2020-11-22 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersPRs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
