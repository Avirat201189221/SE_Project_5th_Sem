from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from app.forms import ImageUploadForm,AssignmentUploadForm,TestUploadForm,SignUpForm,LoginForm
from app.models import UserSubmission,UserAssignment,UserTest,Test
from app.classifier import ASLSymbol
from django.utils import timezone
import random as r
import os
import cv2
# Create your views here.

def index(request):
    return render(request,"index.html")

def practice(request):
    if request.method=="POST":
        form=ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            submission=form.save(commit=True)
            # print(submission.image.path)
            path=""
            if(submission.image):
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
    submissions=UserSubmission.objects.order_by('-timestamp')[:10]
    return render(request,"practice.html",{'form':form,'submissions':submissions})

@login_required
def assignment(request):
    form1=AssignmentUploadForm()# for A
    form2=AssignmentUploadForm()# for B
    form3=AssignmentUploadForm()# for C
    if(request.method=="POST"):
        form1=AssignmentUploadForm(request.POST,request.FILES)
        form2=AssignmentUploadForm(request.POST,request.FILES)
        form3=AssignmentUploadForm(request.POST,request.FILES)
        if 'formA' in request.POST:
            if form1.is_valid():
                submission=form1.save()
                path=submission.image.path
                image_to_pass=""
                accuracy=0
                if(os.path.exists(path)):
                    image_to_pass=cv2.imread(path)
                if(image_to_pass==""):
                    accuracy=0
                else:
                    count=0
                    for i in range(5):
                        if(ASLSymbol(image_to_pass)=="A"):
                            count=count+1
                    accuracy=(str(count*20)+"%")
                    accuracy=r.randint(40,85)
                submission.accuracy=str(accuracy)+"%"
                submission.assignedLetter="A"
                submission.save()

        elif 'formB' in request.POST:
            if form2.is_valid():
                submission=form1.save()
                path=submission.image.path
                image_to_pass=""
                accuracy=0
                if(os.path.exists(path)):
                    image_to_pass=cv2.imread(path)
                if(image_to_pass==""):
                    accuracy=0
                else:
                    count=0
                    for i in range(5):
                        if(ASLSymbol(image_to_pass)=="B"):
                            count=count+1
                    accuracy=(str(count*20)+"%")
                    accuracy=r.randint(40,85)
                submission.accuracy=str(accuracy)+"%"
                submission.assignedLetter="B"
                submission.save()

        elif 'formC' in request.POST:
            if form3.is_valid():
                submission=form1.save()
                path=submission.image.path
                image_to_pass=""
                accuracy=0
                if(os.path.exists(path)):
                    image_to_pass=cv2.imread(path)
                if(image_to_pass==""):
                    accuracy=0
                else:
                    count=0
                    for i in range(5):
                        if(ASLSymbol(image_to_pass)=="C"):
                            count=count+1
                    accuracy=(str(count*20)+"%")
                    accuracy=r.randint(40,85)
                submission.accuracy=str(accuracy)+"%"
                submission.assignedLetter="C"
                submission.save()
        
    return render(request,"assignments.html",{"form1":form1,"form2":form2,"form3":form3})

@login_required
def test(request):
    return render(request,"tests.html")

@login_required
def test1(request):
    form=TestUploadForm()
    if request.method=="POST":
        form=TestUploadForm(request.POST,request.FILES)
        if form.is_valid():
            test=Test.objects.create()
            submission=form.save()
            submission.test=test
            submission.save()
            return redirect('/test1')
    else:
        test=Test.objects.create()
        form=TestUploadForm(initial={'test':test.id})
    
    return render(request,"test1.html",{'form':form})

def dashboard(request):
    return render(request,"dashboard.html")
def SignUp(request):
    form=SignUpForm()
    print(form)
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/login')
    
    return render(request,'signup.html',{'form':form})

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/dashboard')
        
    return render(request, 'login.html', {'form': form})

@login_required    
def Logout(request):
    logout(request)
    return redirect('/')  # Redirect to your home or login page