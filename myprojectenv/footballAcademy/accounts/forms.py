# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    academy_code = forms.CharField(max_length=10, required=True)
    CHOICES = [('player', 'Player'), ('coach', 'Coach')]
    role = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth', 'role', 'bio', 'academy_code']

class UpdateBioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
        }
