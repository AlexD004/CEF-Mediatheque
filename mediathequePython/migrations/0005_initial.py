# Generated by Django 5.1.3 on 2024-12-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mediathequePython', '0004_delete_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=75)),
                ('available', models.BooleanField(default=True)),
                ('details', models.TextField(max_length=300)),
            ],
        ),
    ]
