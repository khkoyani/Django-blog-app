from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # validation is done with UserCreationForm validation protocol
    # storage is done to the User model but only when form.save() is used


class UserUpdateForm(forms.ModelForm):
    # email=forms.EmailField(required=True)
            # Can cross that line out. dont need it now because inheriting from UserModel.
            # Above class inherited from Usercreationform which didnt have a email field
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']

