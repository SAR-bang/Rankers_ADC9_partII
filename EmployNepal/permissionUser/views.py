from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def Permission_postjobs(request):
    try:
        permission_obj = Permission.objects.get(codename = 'can_post_job')
        Company1 = User.objects.create(username = 'Comapny1')
        Company1.user_permissions.add(permission_obj)

        print(Company1.user_permissions.all())
        return HttpResponse("Permission is given to comapany class")

    except:
            return HttpResponse("Error Raised  while assigning the permissions")
            

