# Generated by Django 3.1.13 on 2022-05-10 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_worked', models.PositiveIntegerField()),
                ('hourly_pay_rate', models.PositiveIntegerField()),
                ('overtime_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('overtime_multiplier', models.FloatField(blank=True, null=True)),
                ('annual_gross_pay', models.PositiveIntegerField(blank=True, null=True)),
                ('addcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.addcategory')),
            ],
            options={
                'verbose_name': 'Set Salary',
                'verbose_name_plural': 'Set Salaries',
            },
        ),
    ]
