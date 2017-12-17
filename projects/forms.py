from django import forms
from .models import Project
from clients.models import Client

class NewProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'description'}))

    class Meta:
        model = Project
        fields = ('name', 'description', 'stakeholders')