# Generated by Django 3.1.13 on 2021-09-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='fcm_token',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='fcm_token',
            field=models.TextField(default=''),
        ),
    ]