# Generated by Django 4.0.6 on 2022-10-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='leave_allocation_days',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]