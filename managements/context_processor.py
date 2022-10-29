from multiprocessing import context
from accounts.models import User
from directors.models import Director
from managements.models import Employee


def employee_context(request):
    e = Employee.objects.all().get(user=request.user)
    if e:
        context = {
        'e':e,
        }
        return context
    else:
        user = User.objects.get(id=request.user.id)    
        return user
    