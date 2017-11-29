from django import forms
from django.contrib.auth.models import User
from .models import *


#TODO: date picker

class NewSOGForm(forms.ModelForm):
    class Meta:
        model = slabOnGrade
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NewSOGForm, self).__init__(*args, **kwargs)

        self.fields['budget_id'].widget.attrs={
            'id': 'BudgetId',
            'class': 'form-control',
            'aria-describedby': 'BudgetID',
            'placeholder': 'Enter Budget Number'
        }
        self.fields['sog_slab_description'].widget.attrs={
            'class': 'form-control',
            'id': 'SlabDescription',
            'placeholder': 'Slab Description'
        }
        self.fields['sog_grading_material_thickness'].widget.attrs={
            'class': 'form-control',
            'id': 'MaterialThickness',
            'placeholder': 'Grading Material Thickness'
        }
        self.fields['sog_thickness'].widget.attrs={
            'class': 'form-control',
            'id': 'Thickness',
            'placeholder': 'Thickness'
        }
        self.fields['sog_width'].widget.attrs={
            'class': 'form-control',
            'id': 'Width',
            'placeholder': 'Width'
        }
        self.fields['sog_length'].widget.attrs={
            'class': 'form-control',
            'id': 'Length',
            'placeholder': 'Length',
        }
        self.fields['sog_area'].widget.attrs={
            'class': 'form-control',
            'id': 'Area',
            'placeholder': 'Area'
        }
        self.fields['sog_perimeter'].widget.attrs={
            'class': 'form-control',
            'id': 'Perimeter',
            'placeholder': 'Perimeter'
        }
        self.fields['sog_concrete_mix'].widget.attrs={
            'class': 'form-control',
            'id': 'ConcreteMix',
            'placeholder': 'Concrete Mix'
        }
        self.fields['sog_additive'].widget.attrs={
            'class': 'form-control',
            'id': 'Additive',
            'placeholder': 'Additive'
        }
        self.fields['sog_second_additive'].widget.attrs={
            'class': 'form-control',
            'id': 'SecondAdditive',
            'placeholder': 'Second Additive'
        }
        self.fields['sog_cure'].widget.attrs={
            'class': 'form-control',
            'id': 'Cure',
            'placeholder': 'Cure'
        }
        self.fields['sog_perimeter_forms'].widget.attrs={
            'class': 'form-control',
            'id': 'PerimeterForms',
            'placeholder': 'Perimeter Forms'
        }
        self.fields['sog_bulk_heads'].widget.attrs={
            'class': 'form-control',
            'id': 'BulkHeads',
            'placeholder': 'Bulk Heads',
        }
        self.fields['sog_vapor_barrier'].widget.attrs={
            'class': 'form-control',
            'id': 'VaporBarrier',
            'placeholder': 'Vapor Barrier'
        }
        self.fields['sog_grading_material'].widget.attrs={
            'class': 'form-control',
            'id': 'GradingMaterial',
            'placeholder': 'Grading Material'
        }
        self.fields['sog_anchor_bolts'].widget.attrs={
            'class': 'form-control',
            'id': 'AnchorBolts',
            'placeholder': 'Anchor Bolts'
        }
        self.fields['sog_subcontractor_first'].widget.attrs={
            'class': 'form-control',
            'id': 'FirstSubcontractor',
            'placeholder': 'First Subcontractor'
        }
        self.fields['sog_subcontractor_second'].widget.attrs={
            'class': 'form-control',
            'id': 'SecondSubcontractor',
            'placeholder': 'Second Subcontractor'
        }
        self.fields['sog_subcontractor_third'].widget.attrs={
            'class': 'form-control',
            'id': 'ThirdSubcontractor',
            'placeholder': 'Third Subcontractor'
        }

class NewGeneralConditionForm(forms.ModelForm):
    # Form fields go here if we use custom validators
    class Meta:
        model = GeneralConditions
        fields = '__all__'

    # overload django's widget styling for the footing input form
    def __init__(self, *args, **kwargs):
        super(NewGeneralConditionForm, self).__init__(*args, **kwargs)

        self.fields['budget_id'].widget.attrs={
            'id': 'recipient-name',
            'class': 'form-control',
        }
        self.fields['general_conditions_budget_code'].widget.attrs={
            'id': 'recipient-name',
            'class': 'form-control',
        }
        self.fields['general_conditions_cost'].widget.attrs={
            'id': 'recipient-name',
            'class': 'form-control',
        }
        self.fields['general_conditions_description'].widget.attrs={
            'id': 'message-text',
            'class': 'form-control',
        }
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
        self.fields['budget_id'].widget.attrs={
            'id': 'footing_description',
            'class': 'form-control',
            'aria-describedby': 'basic-addon3'
        }
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
