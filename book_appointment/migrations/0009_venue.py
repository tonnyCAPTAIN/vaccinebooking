# Generated by Django 3.2 on 2021-09-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_appointment', '0008_alter_book_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(choices=[('KNH', 'Kenyatta hsp'), ('MGT', 'Mbagathi hsp'), ('PMW', 'Pumwani hsp'), ('NRB', 'Nairobi hsp'), ('KKG', 'Kakamega hsp')], max_length=30)),
            ],
        ),
    ]
