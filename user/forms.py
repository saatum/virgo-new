from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=20)
    sex = forms.CharField(max_length=9)
    education = forms.CharField(max_length=100)
    residency = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email',  'full_name',
                  'sex', 'education', 'residency']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
