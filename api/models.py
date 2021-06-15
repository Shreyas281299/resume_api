from django.db import models
import os
from .doc_exc import get_info
from django.urls import reverse
# Create your models here.

class Resume(models.Model):
    BASE_DIR = str(os.getcwd())
    Name = models.CharField(max_length=200)
    resume = models.FileField(upload_to='Resume')

    def str(self):
        return self.Name
 
    def phone(self):
        file_path = self.resume.path
        _,phone = get_info(file_path)
        return phone
    def email(self):
        file_path = self.resume.path
        email,_ = get_info(file_path)
        return email
    
        
