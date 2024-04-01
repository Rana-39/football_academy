from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    academy_code = forms.CharField(max_length=10, required=True)  # Add this field for the academy code

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'profile_picture', 'date_of_birth', 'bio', 'academy_code')
