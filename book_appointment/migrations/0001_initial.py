# Generated by Django 3.2 on 2021-05-31 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=70)),
                ('Middle_name', models.CharField(max_length=70)),
                ('Last_name', models.CharField(max_length=70)),
                ('Occupation', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('Very urgent', 'Morning'), ('Urgent', 'Mid-morning'), ('Medium', 'Afternoon'), ('Low', 'Evening')], default='urgent', max_length=12)),
                ('doctor', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book_appointment.profile')),
            ],
        ),
    ]
