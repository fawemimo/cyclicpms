# Generated by Django 4.0.6 on 2022-10-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]