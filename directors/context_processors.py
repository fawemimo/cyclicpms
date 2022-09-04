import imp
from multiprocessing import context
import re
from accounts.models import User
from directors.models import Director
from django.shortcuts import render

def directors(request):
    
    
    context = { 
        'directors':Director(request)
    }
    return context