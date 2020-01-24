from django.db import models

class Job(models.Model):
    job_Title= models.CharField(max_length=40)
    job_discription=models.CharField(max_length=100)
    job_Catagory= models.CharField(max_length=40)

    def __str__(self):
        return self.job_Title + " " + self.job_discription+" "+ self.job_Catagory

     # we can create add permission features using  class Meta

    class Meta :
        permissions = (("can_post_job", "Can post a job"),)
        
class Resume(models.Model):
    name = models.CharField(max_length = 50)
    user = models.CharField(max_length = 50)
    resume = models.FileField(upload_to= 'resume/pdfs')
    resume_QRcode = models.ImageField(upload_to = 'resume/images', null=True, blank = True)


    def __str__(self):
        return f"  the resume name is {self.name} "

    class Meta : 
        permissions = (("uploadResume","can upload Resume"),("modifyResume","can modify Resume"),)

    # Now since we have created custom permission in the permission models to give permission on the basis of the user  we prefer
=======
  
  # custom permission for the model
#   class Meta:
#         permissions = [
#         ("change_task_status", "Can change the status of tasks"),
#         ("popup_task", "Can remove a task by setting its status as closed"),
#         ]
    
