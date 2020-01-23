from django.db import models

class Job(models.Model):
    job_Title= models.CharField(max_length=40)
    job_discription=models.CharField(max_length=100)
    job_Catagory= models.CharField(max_length=40)

    def __str__(self):
        return self.job_Title + " " + self.job_discription+" "+ self.job_Catagory

class Resume(models.Model):
    name = models.CharField(max_length = 50)
    user = models.CharField(max_length = 50)
    resume = models.FileField(upload_to= 'resume/pdfs')
    resume_QRcode = models.ImageField(upload_to = 'resume/images', null=True, blank = True)


    def __str__(self):
        return f"  the resume name is {self.name} "
  
  # custom permission for the model
#   class Meta:
#         permissions = [
#         ("change_task_status", "Can change the status of tasks"),
#         ("popup_task", "Can remove a task by setting its status as closed"),
#         ]
    