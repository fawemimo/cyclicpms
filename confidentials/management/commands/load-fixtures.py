from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_users.json")
        call_command("loaddata", "db_director.json")
        call_command("loaddata", "db_department.json")
        call_command("loaddata", "db_employee.json")
        call_command("loaddata", "db_jobrole.json")
        call_command("loaddata", "db_paygrade.json")
        call_command("loaddata", "db_paygroup.json")
        call_command("loaddata", "db_employee_data.json")
        call_command("loaddata", "db_payment_attribute.json")
        call_command("loaddata", "db_deductionattributevalue.json")
        call_command("loaddata", "db_deductionattributevalues.json")
        call_command("loaddata", "db_salaryattributevalue.json")
        call_command("loaddata", "db_salaryattributevalues.json")
        
