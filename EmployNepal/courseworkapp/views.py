from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage


def create_job(request):
    return render(request,'create_job.html')
    

def save(request):
    if request.method == "POST":
        get_all = request.POST
        get_job_Title = request.POST['job_Title']
        print(get_job_Title)
        get_job_discription = request.POST['job_discription']
        get_job_Catagory = request.POST['job_Catagory']
        print( get_job_Catagory)
        Job_obj = Job(job_Title=get_job_Title,job_discription=get_job_discription,job_Catagory=get_job_Catagory)
        Job_obj.save()
        return render(request,"index.html",{
        'Jobs':Job.objects.all()
        })
    else:
        return HttpResponse("Error record saving")


def view_Jobdata_delete(request, ID):
    print(ID)
    Jobs= Job.objects.get(id=ID)
    print(Jobs)
    Jobs.delete()
    return render(request,"index.html",{
        'Jobs':Job.objects.all()
    }) 

def view_Jobdata_updateform(request,ID):
    print(ID)
    Jobs= Job.objects.get(id=ID)
    print(Jobs)
    context_varible = {
        'Job':Jobs
    }
    return render(request,'update_job.html',context_varible)


def view_update_PostJob(request,ID):
    Jobs= Job.objects.get(id=ID)
    print(Jobs)
    Jobs.job_Title = request.POST['job_Title']
    Jobs.job_discription =request.POST['job_discription']
    Jobs.job_Catagory = request.POST['job_Catagory']
    print(Jobs)
    Jobs.save()
    return render(request,"index.html",{
        'Jobs':Job.objects.all()
    })
def upload_Resume(request):
    return render(request, 'resume.html')

def save_Resume(request):
    context = {}
    if request.method == 'POST':
        get_resume = request.FILES['Resume']
        get_image = request.FILES['imageQR']
        get_name = request.POST['filename']
        get_user = request.POST['username']
        fs = FileSystemStorage()

        name_resume = fs.save(get_resume.name, get_resume)
        name_image = fs.save(get_image.name, get_image)
         
        print(fs.url(name_resume))

        form = Resume( name = get_name, user = get_user  , resume = get_resume, resume_QRcode = get_image)
        form.save()

        # uploaded_resume = request.FILES['Resume']
        
        # context['url'] = fs.url(name)
    else:
        form = Resume()
    return render(request, 'resume.html', {'form':form})



def resumes_list(request):
    pdfs = Resume.objects.all()
    context = {
        'pdfs' : pdfs
    }
    return render(request, 'resumelist.html',context)


def searchResume(request):
    resumetitle = request.GET['Search']

    obj = Resume.objects.filter(name = resumetitle)

    print(obj)

    return render(request, 'resumelist.html', {'pdfs':obj})
