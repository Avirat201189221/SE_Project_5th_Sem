from django import forms
from app.models import UserSubmission

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=UserSubmission
        fields=['image']