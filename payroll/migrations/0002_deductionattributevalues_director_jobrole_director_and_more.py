# Generated by Django 4.0.6 on 2022-10-03 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('set_salary', '0002_alter_deductionattributevalue_attribute_value_and_more'),
        ('directors', '0001_initial'),
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deductionattributevalues',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directors.director'),
        ),
        migrations.AddField(
            model_name='jobrole',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directors.director'),
        ),
        migrations.AddField(
            model_name='paygrade',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directors.director'),
        ),
        migrations.AddField(
            model_name='paygroup',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directors.director'),
        ),
        migrations.AddField(
            model_name='salaryattributevalues',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='directors.director'),
        ),
        migrations.AlterField(
            model_name='deductionattributevalues',
            name='deduction_attribute_value',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='salaryattributevaluess', to='set_salary.deductionattributevalue'),
        ),
        migrations.AlterField(
            model_name='salaryattributevalues',
            name='salary_attribute_value',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='salaryattributevaluess', to='set_salary.salaryattributevalue'),
        ),
    ]