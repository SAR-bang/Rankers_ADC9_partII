from django.shortcuts import render

from django.urls import path,include
from .views import *
from EmployNepal.views import *

urlpatterns = [
    path('createjob/',create_job, name='create_job'),
    path('createjob/save', save),
    path('delete/<int:ID>',view_Jobdata_delete),
    path('edit/<int:ID>',view_Jobdata_updateform),
    path('edit/update/<int:ID>',view_update_PostJob),
    path('uploadResume/', upload_Resume, name='uploadResume'),
    path('uploadResume/savedata', save_Resume),
    path('uploadResume/download',resumes_list),
    path('uploadResume/search',searchResume),
    path('uploadResume/download/search',searchResume),
    path('uploadResume/savedata/search',searchResume),
]
