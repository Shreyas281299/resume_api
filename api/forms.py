from django import forms
from .models import Resume

class resumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('Name','resume')