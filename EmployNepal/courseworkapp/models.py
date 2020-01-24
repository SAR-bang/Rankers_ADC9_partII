from django.db import models
from django.contrib.auth.models import User
import datetime

class Job(models.Model):
    job_Title= models.CharField(max_length=40)
    job_discription=models.CharField(max_length=100)
    job_Catagory= models.CharField(max_length=40)

    def __str__(self):
        return self.job_Title + " " + self.job_discription+" "+ self.job_Catagory

     # we can create add permission features using  class Meta

    class Meta :
        permissions = (("can_post_job", "Can post a job"),)

    def is_valid_job(self):
        return self.job_Title!=None

    def is_valid_catagory(self):
        catagory_list = ['it',"doctor","teacher"]

        return (self.job_Catagory.lower()) in catagory_list
    
        
class Resume(models.Model):
    name = models.CharField(max_length = 50)
    user = models.CharField(max_length = 50)
    resume = models.FileField(upload_to= 'resume/pdfs')
    resume_QRcode = models.ImageField(upload_to = 'resume/images', null=True, blank = True)
    YearUploaded = models.DateField(null = True)


    def __str__(self):
        return f"  the resume name is {self.name} "

    class Meta : 
        permissions = (("uploadResume","can upload Resume"),("modifyResume","can modify Resume"),)

    # Now since we have created custom permission in the permission models to give permission on the basis of the user  we prefer
  
  # custom permission for the model
#   class Meta:
#         permissions = [
#         ("change_task_status", "Can change the status of tasks"),
#         ("popup_task", "Can remove a task by setting its status as closed"),
#         ]
    
    def is_valid_date(self):
        yearUp = int(self.YearUploaded.strftime('%Y'))
        currentYear = int(datetime.datetime.now().year)
        if(yearUp<=currentYear):
            difference = yearUp - currentYear
            return difference <5

    def is_valid_format(self):
        url =  str(self.resume)
        list1 = url.split(".")
        format = list1[-1]
        return format=="pdf"

       
class JobSeeker(models.Model):
    seeker = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    resumes = models.ForeignKey(Resume, on_delete = models.CASCADE, related_name = "resumes")
    def __str__(self):
        return f"the job seeker is {self.seeker}"
    def is_valid_jobseeker(self):
        return self.name!=None

class Company(models.Model):
    company_name = models.CharField(max_length = 50)
    place = models.CharField(max_length = 50)
    jobs = models.ManyToManyField(Job)

    def companyLocation_exist(self):
        return self.company_name != None
    

class Posts(models.Model):
    post_title = models.CharField(max_length = 100)
    jobs = models.ManyToManyField(Job)
    company = models.ForeignKey(Company, on_delete= models.CASCADE, related_name = "companies")
    
    def is_valid_post(self):
        return self.post_title != None


 
        