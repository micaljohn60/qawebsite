from django import forms
from .import models

class GiveSolution(forms.ModelForm):
    class Meta:
        model = models.Solutions
        fields = ['solution']
        
class AskQuestion(forms.ModelForm):
    class Meta:
        model = models.Questions
        fields = ['title','detail']