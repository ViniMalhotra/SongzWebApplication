# Generated by Django 2.1.1 on 2018-09-30 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playsong',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]