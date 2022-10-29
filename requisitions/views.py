from django.shortcuts import render
from django.http import HttpResponse


def req_apply(request):
    return render(request, 'requisitions/select_type.html')