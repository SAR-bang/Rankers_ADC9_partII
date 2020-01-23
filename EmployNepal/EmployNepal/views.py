from django.shortcuts import render
from courseworkapp.models import *
from django.http import HttpResponse

def index(request):
    Job_obj = Job.objects.all()
    print(Job_obj)
    context_varible = {
        'Jobs':Job_obj
    }
    return render(request,'index.html',context_varible)


