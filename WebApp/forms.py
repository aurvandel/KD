from django import forms
from django.contrib.auth.models import User
from .models import *

class NewFootingForm(forms.ModelForm):
    # Form fields go here if we use custom validators
    class Meta:
        model = openBudgets.footings
        fields = '__all__'

    # overload django's widget styling for the footing input form
    def __init__(self, *args, **kwargs):
        super(NewFootingForm, self).__init__(*args, **kwargs)
        self.fields['footing_description'].widget.attrs={
            'id': 'footing_description',
            'class': 'form-control',
            'aria-describedby': 'basic-addon3'
        }
        self.fields['footing_type'].widget.attrs={
            'id': 'footing_description',
            'class': 'form-control',
            'aria-describedby': 'Text input with segmented button dropdown'
        }
        self.fields['footing_width'].widget.attrs={
            'class': 'form-control',
            'id': 'footing_width',
            'aria-describedby': 'basic-addon3'
        }
        self.fields['footing_depth'].widget.attrs={
            'class': 'form-control',
            'id': 'footing_width',
            'aria-describedby': 'basic-addon3'
        }
        self.fields['footing_length'].widget.attrs={
            'class': 'form-control',
            'id': 'footing_width',
            'aria-describedby': 'basic-addon3'
        }
        self.fields['footing_area'].widget.attrs={
            'class': 'form-control',
            'id': 'footing_width',
            'aria-describedby': 'basic-addon3'
        }
        self.fields['footing_concrete_mix'].widget.attrs={
            'class': 'form-control',
            'id': 'footing_width',
            'aria-describedby': 'basic-addon3'
        }
        self.fields['footing_concrete_grout'].widget.attrs={
            'class': 'form-control',
            'id': 'footing_width',
            'aria-describedby': 'basic-addon3'
        }
        self.fields['footing_lumber'].widget.attrs={
            'class': 'form-control',
            'aria-label': 'Text input with segmented button dropdown'
        }
        self.fields['footing_misc_materials'].widget.attrs={
            'class': 'form-control',
            'id': 'footing_width',
            'aria-describedby': 'basic-addon3'
        }

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
