from contacts.forms import SubscribersForm
from .views import subscribers

def email_subscriber(request):
    form = SubscribersForm(request.POST or None)
    context = {
        'email': form
    }
    return context


# def email(request):
#     return {
#         'form':subscribers(request)
#     }