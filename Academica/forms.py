from django import forms
from .models import *


class TutoringForm(forms.ModelForm):
    class Meta:
        model = Tutoring
        fields = ['theme', 'date_requested', 'planned_date', 'qualification', 'feedback', 'state']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['dni','name', 'last_name', 'email', 'password']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'tutor']

    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields['tutor'].queryset = User.objects.filter(rol='Tutor')

class CycleForm(forms.ModelForm):
    class Meta:
        model = Cycle
        fields = ['number', 'parallel', 'subjects']

class CareerForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = ['name', 'cycles']