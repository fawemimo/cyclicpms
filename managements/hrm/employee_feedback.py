from django.http import HttpResponse
from django.shortcuts import redirect,render

from directors.models import Director
from leave.models import FeedBackEmployee
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


"""
 EMPLOYEE FEEDBACK 

"""
def employee_feedback_message(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:
        # company_id              = Company.objects.get(id)
        director = Director.objects.get(user=request.user.id)
        feedbacks = FeedBackEmployee.objects.filter(
            employee__director=director).order_by('-created_at')

        paginator = Paginator(feedbacks, 25)
        page = request.GET.get('page')
        paged_feedbacks = paginator.get_page(page)
        context = {
            'feedbacks': paged_feedbacks,
        }
        return render(request, 'managements/director_template/employee_feedback.html', context)



""" 
FEEDBACK REPLY
"""

@csrf_exempt
def employee_feedback_message_replied(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        feedback_id = request.POST.get('id')
        feedback_reply = request.POST.get('message')

        try:
            feedbackemployee = FeedBackEmployee.objects.get(id=feedback_id)

            feedbackemployee.feedback_reply = feedback_reply
            feedbackemployee.save()
            return HttpResponse('True')
        except:
            return HttpResponse('False')


""" 
SEARCH BAR FOR FEEDBACK
"""            
def search_feedback(request):
    if not request.user.user_type == 5:
        return HttpResponse('You are not allow to view this page')
    else:

        if 'keywords' in request.GET:
            keywords = request.GET['keywords']
            if keywords:
                director = Director.objects.get(user=request.user.id)
                feedbacks = FeedBackEmployee.objects.filter(employee__director=director).order_by('-created_at').filter(
                    Q(employee__user__first_name__icontains=keywords) | Q(feedback__icontains=keywords) | Q(employee__user__last_name__icontains=keywords))

                paginator = Paginator(feedbacks, 25)
                page = request.GET.get('page')
                paged_feedbacks = paginator.get_page(page)
                total = feedbacks.count()

            context = {
                'total': total,
                'feedbacks': paged_feedbacks,

                # 'directors':directors
            }

        return render(request, 'managements/director_template/employee_feedback.html', context)




