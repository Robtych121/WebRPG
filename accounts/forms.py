from django import forms
from django.contrib.auth.models import User

class ModificationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']