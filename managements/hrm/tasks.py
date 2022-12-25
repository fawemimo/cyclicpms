from datetime import datetime
from celery import shared_task
from django.db import transaction
from leave.models import LeaveReportEmployee


@shared_task()
def leave_management():

    """
    LEAVE EMPLOYEE MANAGEMENT TO DETERMINE THE START OF THE DATE AND THE END OF THE DATE
    """
    with transaction.atomic():
        on_leave = LeaveReportEmployee.objects.filter(is_requesting=True)

        today_date = datetime.now()

        for leave in on_leave:
            if leave.is_on_leave:

                if leave.leave_end < today_date:
                    leave.is_on_leave = False
                    leave.is_requesting = False

                else:

                    if leave.leave_start <= today_date:
                        leave.is_on_leave = True
                    else:
                        leave.is_on_leave = False

            leave.save()
