# Generated by Django 5.1.4 on 2025-01-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticMediatheque', '0012_alter_author_name_alter_director_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medias',
            name='timeLoan',
            field=models.IntegerField(null=True),
        ),
    ]
