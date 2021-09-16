from django.shortcuts import render

# Create your views here.

def bank(request):
    return render(request,'confidentials/bank.html')