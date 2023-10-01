from django import forms
from .models import AcademicSession

class AcademicSessionForm(forms.ModelForm):
    class Meta:
        model= AcademicSession
        fields=['session_name','start_date','end_date']