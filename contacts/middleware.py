from django.db.models import F

from contacts.models import Newstats


class StatsMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        # print('one time')
        
    def stats(self,os_info)    :
        if 'Windows' in os_info:
            Newstats.objects.all().update(win=F('win')+1)
        elif 'mac' in os_info:
            Newstats.objects.all().update(mac=F('mac')+1)
        elif 'linux' in os_info:
            Newstats.objects.all().update(linux=F('linux')+1)    
        elif 'iphone' in os_info:
            Newstats.objects.all().update(iph=F('iph')+1)
        elif 'Android' in os_info:
            Newstats.objects.all().update(android=F('android')+1)    
        else:
            Newstats.objects.all().update(oth=F('oth')+1)    
             
        
    def __call__(self, request):
        if "admin" not in request.path:
            self.stats(request.META['HTTP_USER_AGENT'])

        response = self.get_response(request)
        
        # print('hello World')
        # print(request.META['REQUEST_METHOD'])
        # print(request.META['HTTP_USER_AGENT'])
        # response = self.get_response(request)
        # print('after')
        return response
        