# Generated by Django 5.1.4 on 2024-12-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticMediatheque', '0008_alter_medias_mediatype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('canLoan', models.BooleanField()),
                ('numLoan', models.IntegerField()),
            ],
        ),
    ]