from django import forms
from app.models import UserSubmission,UserAssignment,UserTest

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
        fields=['test','zip_file','time_secs']
        widgets={
            'test':forms.HiddenInput(),
            'time_secs':forms.HiddenInput(),
        }