from django.db import models
from PIL import Image
# from app.classifier import ASLSymbol
import numpy as np
# Create your models here.
class UserSubmission(models.Model):
    image = models.ImageField(upload_to='',blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=50, blank=True)

class UserAssignment(models.Model):
    image=models.ImageField(upload_to='',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    assignedLetter=models.CharField(max_length=50,blank=True)
    accuracy=models.CharField(max_length=50,blank=True)
    feedback=models.CharField(max_length=500,blank=True)

class Test(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)

class UserTest(models.Model):
    test=models.ForeignKey(Test,on_delete=models.CASCADE)
    zip_file=models.FileField(upload_to='zipfiles')
    time_secs=models.IntegerField(null=True,blank=True)
