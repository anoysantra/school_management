from django import forms
from .models import Exams

class ExamForm(forms.ModelForm):
    class Meta:
        model= Exams
        fields=['exam_name','full_marks']