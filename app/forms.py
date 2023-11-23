from django import forms
from app.models import UserSubmission,UserAssignment,UserTest
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=UserSubmission
        fields=['image']

class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model=UserAssignment
        fields=['image']

class TestUploadForm(forms.ModelForm):
    class Meta:
        model=UserTest
        fields=['test','zip_file']
        widgets={
            'test':forms.HiddenInput(),
            # 'time_secs':forms.HiddenInput(),
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2')

class LoginForm(AuthenticationForm):
    model=User
    fields=('username','password')