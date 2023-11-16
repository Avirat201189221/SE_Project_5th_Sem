from django import forms
from app.models import UserSubmission,UserAssignment

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=UserSubmission
        fields=['image']

class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model=UserAssignment
        fields=['image']