from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class UserProfileInfo(models.Model):

    # Create relationship (doesnt inherit from User
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class openBudgets(models.Model):
    TAX_EXEMPT = '*'
    NOT_TAX_EXEMPT = ''
    IN_PROGRESS = 'IP'
    READY_TO_REVIEW = 'RTR'
    REVIEWED = 'RV'
    COMPLETE = 'CMP'
    BUDGET_STATUS_CHOICES = (

        (IN_PROGRESS, 'In Progress'),
        (READY_TO_REVIEW, 'Ready To Review'),
        (REVIEWED, 'Reviewed'),
        (COMPLETE, 'Completed'),

    )

    TAX_EXEMPT_CHOICES = (

        (TAX_EXEMPT, '*'),
        (NOT_TAX_EXEMPT, '')

    )


    budget_id = models.PositiveIntegerField(unique = True)
    # Created and modified fields will be auto populated
    created = models.DateField(auto_now_add=True, editable=False)
    project_name = models.CharField(max_length = 255, unique = True)
    city = models.CharField(max_length = 35, unique = False)
    state = models.CharField(max_length = 35, unique = False)
    internal_due_date = models.DateField()
    external_due_date = models.DateField()
    estimator = models.CharField(max_length = 50, unique = False)
    budget_amount = models.DecimalField(max_digits = 15, decimal_places = 8)
    budget_complete = models.CharField(

        max_length = 3,
        choices = BUDGET_STATUS_CHOICES,
        default = IN_PROGRESS

    )

    revised_date = models.DateField(auto_now=True, editable=False)
    general_contractor = models.CharField(max_length = 50, unique = False)
    tax_exempt_status = models.CharField(

        max_length = 1,
        unique = False,
        choices = TAX_EXEMPT_CHOICES,
        default = NOT_TAX_EXEMPT

    )

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of a budget.
         """
         return reverse('budget-detail', args=[str(self.id)])

    def __str__(self):
        return self.project_name

    # def save(self, *args, **kwargs):
    #     # On save, update timestamps
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.revised_date = timezone.now()
    #     return super(openBudgets, self).save(*args, **kwargs)

    class Meta:
        # orders data
        ordering = ['-budget_id']

    class castInPlace(models.Model):
        panel_id = models.PositiveIntegerField(primary_key = True, unique = True)
        panel_description = models.CharField(max_length = 255, unique = False)
        budget_id = models.ForeignKey('openBudgets', on_delete = models.CASCADE)
        panel_quantity = models.PositiveSmallIntegerField()
        panel_thickness = models.DecimalField(max_digits = 10, decimal_places = 3)
        panel_length = models.DecimalField(max_digits = 10, decimal_places = 3)
        panel_height = models.DecimalField(max_digits = 10, decimal_places = 3)
        panel_contact_area = models.DecimalField(max_digits = 10, decimal_places = 3)
        wall_area = models.DecimalField(max_digits = 10, decimal_places = 3)
        wall_type = models.CharField(max_length = 255, unique = False) #maybe add a list here to restrict user input

        class footings(models.Model):
            footing_id = models.PositiveIntegerField(primary_key = True, unique = True)
            footing_description = models.CharField(max_length = 255, unique = False)
            footing_type = models.CharField(max_length = 255, unique = False)
            footing_width = models.PositiveSmallIntegerField() #width in inches
            footing_depth = models.PositiveSmallIntegerField() #width in inches
            footing_length = models.PositiveSmallIntegerField() #width in feet
            footing_area = models.DecimalField(max_digits = 15, decimal_places = 4)
            footing_concrete_mix = models.CharField(max_length = 255, unique = False) #will eventually be a selection list populated from another table
            footing_concrete_grout = models.CharField(max_length = 255, unique = False) #will eventually be a selection list populated from another table
            footing_lumber = models.CharField(max_length = 255, unique = False) #will eventually be a selection list populated by another table
            footing_misc_materials = models.CharField(max_length = 255, unique = False) #will eventually be selection list populated by another table

            class slabOnGrade(models.Model):
                sog_id = models.PositiveIntegerField(primary_key = True, unique = True)
                sog_grading_material_thickness = models.PositiveSmallIntegerField() #thickness in inches
                sog_thickness = models.PositiveSmallIntegerField() #thickness measured in inches
                sog_width = models.PositiveSmallIntegerField() #measured in feet
                sog_length = models.PositiveSmallIntegerField() #measured in feet
                sog_area = models.DecimalField(max_digits = 15, decimal_places = 4)
                sog_perimeter = models.DecimalField(max_digits = 15, decimal_places = 4)
                sog_concrete_mix = models.CharField(max_length = 60, unique = False) #will eventually be a selection list populated by another table
                sog_additive = models.CharField(max_length = 100, unique = False) #will eventually be a selection list populated by another table
                sog_second_additive = models.CharField(max_length = 100, unique = False) #will eventually be a selection list populated by another table
                sog_cure = models.CharField(max_length = 100, unique = False) #will eventually be a selection list populated by another table
                sog_perimeter_forms = models.CharField(max_length = 100, unique = False) #Need to check to see if this is a length or a description
                sog_bulk_heads = models.CharField(max_length = 100, unique = False) #need to check to see if this is a number or a description
                sog_vapor_barrier = models.CharField(max_length = 100, unique = False) #need to check to see if this is a number or a description
                sog_grading_material = models.CharField(max_length = 100, unique = False) #type of grading material... might be replaced with a list populated from another table
                sog_anchor_bolts = models.CharField(max_length = 100, unique = False) #need to check to see if this is going to be a selection from a list or a description
                #sog_concrete_misc_material #check to see what this is
                #sog_material_misc_material
                sog_subcontractor_first = models.CharField(max_length = 100, unique = False) #probably needs to be populated from another table and be a selection list
                sog_subcontractor_second = models.CharField(max_length = 100, unique = False)#probably needs to be populated from another table and be a selection list
                sog_subcontractor_third = models.CharField(max_length = 100, unique = False)#probably needs to be populated from another table and be a selection list

                class tiltUp(models.Model):
                    tilt_up_panel_id = models.AutoField(primary_key = True, unique = True)
                    tilt_up_panel_description = models.CharField(max_length = 255, unique = False)
                    tilt_up_panel_thickness = models.DecimalField(max_digits = 15, decimal_places = 4) #measured in inches
                    tilt_up_panel_width = models.DecimalField(max_digits = 15, decimal_places = 4) #measred in feet
                    tilt_up_panel_height = models.DecimalField(max_digits = 15, decimal_places = 4) #measured in feet
                    tilt_up_panel_area = models.DecimalField(max_digits = 15, decimal_places = 4)
                    tilt_up_forms = models.DecimalField(max_digits = 15, decimal_places = 4) #measured in linear feet
                    tilt_up_perimeter = models.DecimalField(max_digits = 15, decimal_places = 4) #measured in linear feet
                    tilt_up_gross_sqft = models.DecimalField(max_digits = 15, decimal_places = 4) #measured in sq/ft
                    tilt_up_openings_sqft = models.DecimalField(max_digits = 15, decimal_places = 4)
                    tilt_up_net_sqft = models.DecimalField(max_digits = 15, decimal_places = 4)
                    tilt_up_panel_weight = models.PositiveSmallIntegerField() #measured in tons
                    tilt_up_panel_concrete_mix = models.CharField(max_length = 150, unique = False)
                    tilt_up_panel_additive = models.CharField(max_length = 100, unique = False) #will eventually be a selection list populated by another table
                    tilt_up_panel_second_additive = models.CharField(max_length = 100, unique = False) #will eventually be a selection list populated by another table
                    tilt_up_panel_forms = models.CharField(max_length = 100, unique = False)
                    tilt_up_panel_engineering = models.CharField(max_length = 100, unique = False)
                    tilt_up_panel_crane = models.CharField(max_length = 100, unique = False)
                    tilt_up_panel_caulking = models.CharField(max_length = 100, unique = False)
                    tilt_up_panel_pumping = models.CharField(max_length = 100, unique = False)
                    tilt_up_panel_welding = models.CharField(max_length = 100, unique = False)
                    tilt_up_sack_patch = models.CharField(max_length = 100, unique = False)
                    tilt_up_brace_rental = models.CharField(max_length = 100, unique = False)

                    class mixDesign(models.Model):
                        concrete_mix_id = models.AutoField(primary_key = True, unique = True)
                        concrete_mix_description = models.CharField(max_length = 255, unique = False)
                        concrete_mix_psi = models.PositiveSmallIntegerField()
                        concrete_mix_price = models.DecimalField(max_digits = 15, decimal_places = 4)

