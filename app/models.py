from django.db import models
from PIL import Image
# from app.classifier import ASLSymbol
import numpy as np
# Create your models here.
class UserSubmission(models.Model):
    image = models.ImageField(upload_to='')
    timestamp = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=50, blank=True)