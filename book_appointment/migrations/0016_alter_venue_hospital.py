# Generated by Django 3.2 on 2021-09-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_appointment', '0015_alter_venue_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='hospital',
            field=models.CharField(choices=[('Kenyatta hsp', 'KNH-HSP'), ('Mbagathi hsp', 'MGT-HSP'), ('Pumwani hsp', 'PMW-HSP'), ('Nairobi hsp', 'NRB-HSP'), ('Kakamega hsp', 'KKG-HSP'), ('Aghakan hsp', 'AG-HSP')], default='NRB', max_length=30),
        ),
    ]