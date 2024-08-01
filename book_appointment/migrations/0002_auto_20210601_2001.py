# Generated by Django 3.2 on 2021-06-01 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='profile',
        ),
        migrations.AddField(
            model_name='book',
            name='person',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]