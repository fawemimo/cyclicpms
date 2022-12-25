from multiprocessing import context
from accounts.models import User
from directors.models import Director
from managements.models import Employee


def employee_context(request):
    if request.user.user_type == 1 :
        e = Employee.objects.get(user=request.user)
        if e:
            context = {
            'e':e,
            }
            return context
        else:
            user = User.objects.get(id=request.user.id)    
            return user
    