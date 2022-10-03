from django import forms

class TaskForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
