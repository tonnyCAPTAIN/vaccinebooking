# Generated by Django 3.2 on 2021-09-17 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_appointment', '0011_remove_venue_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='book_appointment.profile'),
        ),
    ]
