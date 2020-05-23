from django import forms
from .models import Character

class NewCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name','gender','role','race']