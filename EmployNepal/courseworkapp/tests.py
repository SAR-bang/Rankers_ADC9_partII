from django.test import TestCase
from .models import Job, Posts, Company,Resume
from django.contrib.auth.models import User

class Setup_Class(TestCase):

    def setUp(self):
        job1 = Job.objects.create(job_Title = "manager", job_discription = 'about job',job_Catagory = 'c1')
        company1 = Company.objects.create(company_name = "Realify",place = "kathmandu")
        Resume1 = Resume.objects.create(name = "Res1", user= "Ram", resume = "path.docx", YearUploaded = "2020-1-20")

    def test_is_valid_job(self):
        job2 = Job.objects.get(job_Title = "manager")
        value=job2.is_valid_job()
        self.assertTrue(value,True)
    
    def test_companyLocation_exist(self):
        company1=Company.objects.get(company_name = "Realify")
        value = company1.companyLocation_exist()
        self.assertTrue(value,True)
    def test_is_valid_date(self):
        Resume1 = Resume.objects.get(name = "Res1")
        value = Resume1.is_valid_date()
        self.assertTrue(value,True)

    def test_is_valid_format(self):
        Resume1 = Resume.objects.get(name = "Res1")
        valuepdf = Resume1.is_valid_format()
        self.assertTrue(valuepdf,True)

    def test_is_validcatagory(self):
        job1 = Job.objects.get(job_Title = "manager")
        value = job1.is_valid_catagory()
        self.assertTrue(value,True)
    

   