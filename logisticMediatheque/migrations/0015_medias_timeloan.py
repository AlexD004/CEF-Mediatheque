# Generated by Django 5.1.4 on 2025-01-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticMediatheque', '0014_remove_medias_timeloan'),
    ]

    operations = [
        migrations.AddField(
            model_name='medias',
            name='timeLoan',
            field=models.IntegerField(null=True),
        ),
    ]