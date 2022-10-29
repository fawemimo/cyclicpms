# Generated by Django 4.0.6 on 2022-10-03 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='directors.director')),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_unique_id', models.CharField(blank=True, max_length=6, unique=True)),
                ('dob', models.DateField(blank=True, help_text='format: Date of Birth', null=True)),
                ('phone_number_2', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_address', models.CharField(blank=True, max_length=255, null=True)),
                ('fcm_token', models.TextField(blank=True, default='', null=True)),
                ('date_employed', models.DateTimeField(auto_now_add=True, verbose_name='Date Employed')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True)),
                ('profile_pic', models.FileField(blank=True, default='avatar.png', null=True, upload_to='media/')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Updated')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='managements.department')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='directors.director')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='UploadEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.FileField(upload_to='employeecreation')),
                ('uploaded', models.DateField(auto_now_add=True)),
                ('activated', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Bulk Creation',
                'verbose_name_plural': 'Bulk Creations',
            },
        ),
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_manager', models.BooleanField(default=False)),
                ('is_supervisor', models.BooleanField(default=False, help_text='format: Supervisor,Team Leader,Head of Department have the same role')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='managements.employee')),
            ],
            options={
                'verbose_name': 'Employee Role',
                'verbose_name_plural': 'Employee Roles',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_unique_id', models.CharField(blank=True, max_length=6)),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone_number_2', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_address', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dapartment/Units')),
                ('fcm_token', models.TextField(blank=True, default='', null=True)),
                ('date_employed', models.DateTimeField(auto_now_add=True, verbose_name='Date Employed')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('profile_pic', models.FileField(blank=True, default='avatar.png', null=True, upload_to='media/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
            },
        ),
    ]
