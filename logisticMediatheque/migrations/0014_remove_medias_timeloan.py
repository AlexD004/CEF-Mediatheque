# Generated by Django 5.1.4 on 2025-01-14 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logisticMediatheque', '0013_medias_timeloan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medias',
            name='timeLoan',
        ),
    ]
