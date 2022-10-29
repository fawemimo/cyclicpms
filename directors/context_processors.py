from directors.models import Director

def directors(request):
    
    
    context = { 
        'directors':Director(request)
    }
    return context