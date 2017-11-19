from django import forms
from django.contrib.auth.models import User
from .models import *

class NewFootingForm(forms.ModelForm):
    # Form fields go here if we use custom validators
    class Meta:
        model = openBudgets.footings
        fields = '__all__'


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta():
#         model = User
#         fields = ('username', 'email', 'password')
#
# class UserProfileInfo(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
