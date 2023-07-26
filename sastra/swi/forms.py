from django import forms
from .models import students

class newdetails(forms.ModelForm):
    class Meta:
        model = students
        fields = ('name', 'password','regno','cgpa','attendance')