from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from .resources import PayrollManagerResources
# from tablib import Dataset
from django.http import HttpResponse


def index(request):
    
    return render(request,'payroll/index.html')


# def payroll_upload(request):
#     if request.method == 'POST':
#         payroll_resource = PayrollManagerResources()
#         dataset = Dataset()
#         files = request.FILES.get('myfile')

#         # if not files.endswith('xlsx'):
#         #     print('wrong file format')
#         #     return render(request,'payroll/upload.html')

#         imported_data = dataset.load(files.read(), format='xlsx')
#         for data in imported_data:
#             value = data[0]    
#             value1 = data[1]
#             value2 = data[2]
#             print(value)
#             print(value2)
#             print(value1)

#     return render(request,'payroll/upload.html')    