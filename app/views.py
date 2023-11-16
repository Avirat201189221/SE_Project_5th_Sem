from django.shortcuts import render,redirect
from app.forms import ImageUploadForm
from app.models import UserSubmission
from app.classifier import ASLSymbol
import os
import cv2
import numpy as np
# Create your views here.
def index(request):
    return render(request,"index.html")

def practice(request):
    if request.method=="POST":
        form=ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            submission=form.save(commit=True)
            # print(submission.image.path)
            path=submission.image.path
            pred=""
            image_to_pass=""
            if(os.path.exists(path)):
                image_to_pass=cv2.imread(path)
            if(image_to_pass==""):
                pred="Incorrect img format"
            else:
                pred=ASLSymbol(image_to_pass)
            submission.prediction=pred
            submission.save()
            return redirect('/practice')
    form=ImageUploadForm()
    submissions=UserSubmission.objects.all()
    return render(request,"practice.html",{'form':form,'submissions':submissions})

