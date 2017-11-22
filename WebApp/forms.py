from django import forms
from django.contrib.auth.models import User
from .models import *


#TODO: date picker

class NewBudgetForm(forms.ModelForm):
    class Meta:
        model = openBudgets
        exclude = [
            'created',
            'revised_date',
            'budget_complete',
            'budget_amount',
            'estimator'
        ]

        widgets = {
            'internal_due_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'external_due_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }
    # overload django's widget styling
    def __init__(self, *args, **kwargs):
        super(NewBudgetForm, self).__init__(*args, **kwargs)
        self.fields['budget_id'].widget.attrs={
            'id': 'BudgetId',
            'class': 'form-control',
            'aria-describedby': 'BudgetID',
            'placeholder': 'Enter Budget Number'
        }
        self.fields['project_name'].widget.attrs={
            'class': 'form-control',
            'id': 'ProjectName',
            'placeholder': 'Project Name'
        }
        self.fields['zip_code'].widget.attrs={
            'class': 'form-control',
            'id': 'ZipCode',
            'placeholder': 'ZipCode'
        }
        self.fields['city'].widget.attrs={
            'class': 'form-control',
            'id': 'City',
            'placeholder': 'City'
        }
        self.fields['state'].widget.attrs={
            'class': 'form-control',
            'id': 'State',
            'placeholder': 'State'
        }
        self.fields['internal_due_date'].widget.attrs={
            'class': 'form-control',
            'id': 'InternalDueDate',
            'placeholder': '',
        }
        self.fields['external_due_date'].widget.attrs={
            'class': 'form-control',
            'id': 'ExternalDueDate',
            'placeholder': ''
        }
        self.fields['general_contractor'].widget.attrs={
            'class': 'form-control',
            'id': 'GeneralContractor',
            'placeholder': 'General Contractor'
        }
        self.fields['tax_exempt_status'].widget.attrs={
            'class': 'form-check-input',
        }

class NewFootingForm(forms.ModelForm):
    # Form fields go here if we use custom validators
    class Meta:
        model = footings
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
        self.fields['footing_subcontractor'].widget.attrs={
            'class': 'form-control',
            'aria-label': 'Text input with segmented button dropdown'
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
