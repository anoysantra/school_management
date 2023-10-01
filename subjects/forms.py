from django import forms
from .models import Subjects

class SubjectsForm(forms.ModelForm):
    class Meta:
        model= Subjects
        fields=['class_name','subjects_name']