from django.shortcuts import render, redirect
from courseworkapp.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def index(request):
    if request.user.is_authenticated:
        print("yes")
    else:
        print("NO")

    Job_obj = Job.objects.all()
    print(Job_obj)
    context_varible = {
        'Jobs':Job_obj
    }
    return render(request,'index.html',context_varible)



def signup(request):
    logout(request,user)
    return render(request, 'signup.html')

def signup_data(request):
    if request.method=='POST':
        get_fullname = request.POST['fullname']
        get_email  = request.POST['email']
        get_username = request.POST['username']
        get_password = request.POST['password']

        user_obj = User.objects.create_user(username=get_fullname,email=get_email,password=get_password)
        return HttpResponse("logged in system")


def loginpage(request):
    return render(request,'login.html')


def loginUser(request):
    if request.method == 'POST':
            user = authenticate(username = request.POST['username'], password = request.POST['password'])
            if user is not None: 
                login(request,user)
                if request.user.is_authenticated:
                    print(request.user)
                    return render(request, 'index.html', {
                    'Jobs' : Job.objects.all() 
                    })
                else:
                    return HttpResponse("your password and username didnot match")



def logoutUser(request):
    logout(request)
    return render(request, 'index.html', {
                'Jobs' : Job.objects.all() 
                })


#from django.contrib.auth.hashers import check_password


# def authenticate(username, password):
#     try:
#         user = User.objects.get(username = username)
#         if check_password(password, user.password):
#             return user 
#     except: 
#         return None

# def login(request,user):
#     request.session['user'] = user.id

# def logout(request):
#     try:
#         del request.session['user']
#     except:
#         pass