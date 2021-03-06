from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class UserProfileInfo(models.Model):

    # Create relationship (doesnt inherit from User)
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class openBudgets(models.Model): #come back in and set appropriate fields to blank=false to force user to input information
    TAX_EXEMPT = '*'
    NOT_TAX_EXEMPT = ''
    IN_PROGRESS = 'In Progress'
    READY_TO_REVIEW = 'Ready For Review'
    REVIEWED = 'Reviewed'
    COMPLETE = 'Complete'
    BUDGET_STATUS_CHOICES = (

        (IN_PROGRESS, 'In Progress'),
        (READY_TO_REVIEW, 'Ready To Review'),
        (REVIEWED, 'Reviewed'),
        (COMPLETE, 'Completed'),

    )

    # TAX_EXEMPT_CHOICES = (
    #
    #     (TAX_EXEMPT, '*'),
    #     (NOT_TAX_EXEMPT, '')
    #
    # )

    # id = models.AutoField(primary_key=True)       id field is handled by django
    budget_id = models.PositiveIntegerField(unique = True)
    zip_code = models.PositiveIntegerField(unique = False)
    # Created and revised_date fields will be auto populated
    created = models.DateField(auto_now_add=True, editable=False)
    project_name = models.CharField(max_length = 255, unique = True)
    city = models.CharField(max_length = 35, unique = False)
    state = models.CharField(max_length = 35, unique = False)
    internal_due_date = models.DateField()
    external_due_date = models.DateField()
    estimator = models.CharField(null = True, blank = True, max_length = 50, unique = False)
    budget_amount = models.DecimalField(null = True, blank = True, max_digits = 15, decimal_places = 8)
    budget_complete = models.CharField(

        max_length = 20,
        choices = BUDGET_STATUS_CHOICES,
        default = IN_PROGRESS

    )
    tax_exempt_status = models.BooleanField()
    revised_date = models.DateField(auto_now=True, editable=False)
    general_contractor = models.CharField(max_length = 50, unique = False)
    # tax_exempt_status = models.CharField(
    #
    #     max_length = 1,
    #     unique = False,
    #     choices = TAX_EXEMPT_CHOICES,
    #     default = NOT_TAX_EXEMPT
    #
    # )

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of a budget.
         """
         return reverse('budget-detail', args=[str(self.id)]) #budget-detail comes form URlS.py

    def __str__(self):
        return self.project_name

    # def save(self, *args, **kwargs):
    #     # On save, update timestamps
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.revised_date = timezone.now()
    #     return super(openBudgets, self).save(*args, **kwargs)

    class Meta:
        # orders data by budget_id in reverse order
        ordering = ['-budget_id']

class castInPlace(models.Model):
    panel_description = models.CharField(max_length = 255, unique = False)
    budget_id = models.ForeignKey(openBudgets, on_delete = models.CASCADE)
    panel_quantity = models.PositiveSmallIntegerField()
    panel_thickness = models.DecimalField(max_digits = 10, decimal_places = 3)
    panel_length = models.DecimalField(max_digits = 10, decimal_places = 3)
    panel_height = models.DecimalField(max_digits = 10, decimal_places = 3)
    panel_contact_area = models.DecimalField(max_digits = 10, decimal_places = 3)
    wall_area = models.DecimalField(max_digits = 10, decimal_places = 3)
    wall_type = models.CharField(max_length = 255, unique = False) #maybe add a list here to restrict user input

    def __str__(self):
        return self.panel_description

    class Meta:
        ordering = ['id']


class footings(models.Model):
    budget_id = models.ForeignKey(openBudgets, on_delete = models.CASCADE)
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
    footing_subcontractor = models.CharField(max_length = 255, unique = False)

    def __str__(self):
        return self.footing_description

    class Meta:
        ordering = ['id']

class slabOnGrade(models.Model):
    budget_id = models.ForeignKey(openBudgets, on_delete = models.CASCADE)
    sog_slab_description = models.CharField(max_length = 255, unique = False)
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

    def __str__(self):
        return self.sog_slab_description

    class Meta:
        ordering = ['id']

class tiltUp(models.Model):
    budget_id = models.ForeignKey(openBudgets, on_delete = models.CASCADE)
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

    def __str__(self):
        return self.tilt_up_panel_description


class slabOnDeck(models.Model):
    budget_id = models.ForeignKey(openBudgets, on_delete = models.CASCADE)
    slab_on_deck_type = models.CharField(max_length = 255, unique = False)
    slab_on_deck_description = models.CharField(max_length = 255, unique = False)
    slab_on_deck_thickness = models.DecimalField(max_digits = 25, decimal_places = 4)
    slab_on_deck_area = models.DecimalField(max_digits = 25, decimal_places = 4)
    slab_on_deck_forms = models.DecimalField(max_digits = 25, decimal_places = 4)
    slab_on_deck_concrete_mix = models.CharField(max_length = 255, unique = False) #need to create additive table or shopping table

    def __str__(self):
        return self.slab_on_deck_description

    class Meta:
        ordering = ['id']

class GeneralConditions(models.Model):
    budget_id = models.ForeignKey(openBudgets, on_delete = models.CASCADE)
    general_conditions_budget_code = models.PositiveIntegerField()
    general_conditions_description = models.TextField()
    general_conditions_cost = models.DecimalField(max_digits = 15, decimal_places = 4)

class WasteCasting(models.Model):
    budget_id = models.ForeignKey(openBudgets, on_delete = models.CASCADE)
    waste_casting_description = models.CharField(max_length=255, unique=False)
    waste_casting_basis = models.CharField(max_length=255, unique=False)
    waste_casting_sqft = models.DecimalField(max_digits=15, decimal_places=4)
    waste_casting_concrete_description = models.CharField(max_length=255, unique=False)     #does this pull from the mixDesign table?
    waste_casting_totalCY = models.PositiveSmallIntegerField()
    waste_casting_psi = models.PositiveSmallIntegerField()
    waste_casting_materials_labor = models.CharField(max_length=255, unique=False)

class mixDesign(models.Model):
    #mix_id = models.AutoField(primary_key=True, default="1")       #id field is handled by django
    concrete_mix_description = models.CharField(max_length = 255, unique = False)
    concrete_mix_psi = models.PositiveSmallIntegerField()
    concrete_mix_price = models.DecimalField(max_digits = 15, decimal_places = 4) 

    def __str__(self):
        return self.concrete_mix_description

class States(models.Model):

    # stateChoices = (
    #     ("Alabama", "Alabama"), ("Alaska", "Alaska"), ("Arizona", "Arizona"), ("Arkansas", "Arkansas"),
    #     ("California", "California"), ("Colorado", "Colorado"), ("Connecticut", "Connecticut"),
    #     ("Delaware", "Delaware"), ("Florida", "Florida"), ("Georgia", "Georgia"), ("Hawaii", "Hawaii"),
    #     ("Idaho", "Idaho"), ("Illinois", "Illinois"), ("Indiana", "Indiana"), ("Iowa", "Iowa"), ("Kansas", "Kansas"),
    #     ("Kentucky", "Kentucky"), ("Louisiana", "Louisiana"), ("Maine", "Maine"), ("Maryland", "Maryland"),
    #     ("Massachusetts", "Massachusetts"), ("Michigan", "Michigan"), ("Minnesota", "Minnesota"),
    #     ("Mississippi", "Mississippi"), ("Missouri", "Missouri"), ("Montana", "Montana"), ("Nebraska", "Nebraska"),
    #     ("Nevada", "Nevada"), ("New Hampshire", "New Hampshire"), ("New Jersey", "New Jersey"),
    #     ("New Mexico", "New Mexico"), ("New York", "New York"), ("North Carolina", "North Carolina"),
    #     ("North Dakota", "North Dakota"), ("Ohio", "Ohio"), ("Oklahoma", "Oklahoma"), ("Oregon", "Oregon"),
    #     ("Pennsylvania", "Pennsylvania"), ("Rhode", "Rhode"), ("Island", "Island"),
    #     ("South Carolina", "South Carolina"), ("South Dakota", "South Dakota"), ("Tennessee", "Tennessee"),
    #     ("Texas", "Texas"), ("Utah", "Utah"), ("Vermont", "Vermont"), ("Virginia", "Virginia"),
    #     ("Washington", "Washington"), ("West Virginia", "West Virginia"), ("Wisconsin", "Wisconsin"),
    #     ("Wyoming", "Wyoming")
    # )
    # StateAbbreviationChoices = (
    #     ("AK", "AK"), ("AL", "AL"), ("AR", "AR"), ("AZ", "AZ"), ("CA", "CA"), ("CO", "CO"), ("CT", "CT"), ("DC", "DC"),
    #     ("DE", "DE"), ("FL", "FL"), ("GA", "GA"), ("GU", "GU"), ("HI", "HI"), ("IA", "IA"), ("ID", 'ID'), ("IL", "IL"),
    #     ("IN", "IN"), ("KS", "KS"), ("KY", "KY"), ("LA", "LA"), ("MA", "MA"), ("MD", "MD"), ("ME", "ME"), ("MH", "MH"),
    #     ("MI", "MI"), ("MN", "MN"), ("MO", "MO"), ("MS", "MS"), ("MT", "MT"), ("NC", "NC"), ("ND", "ND"), ("NE", "NE"),
    #     ("NH", "NH"), ("NJ", "NJ"), ("NM", "NM"), ("NV", "NV"), ("NY", "NY"), ("OH", "OH"), ("OK", "OK"), ("OR", "OR"),
    #     ("PA", "PA"), ("PR", "PR"), ("PW", "PW"), ("RI", "RI"), ("SC", "SC"), ("SD", "SD"), ("TN", "TN"), ("TX", "TX"),
    #     ("UT", "UT"), ("VA", "VA"), ("VI", "VI"), ("VT", "VT"), ("WA", "WA"), ("WI", "WI"), ("WV", "WV"), ("WY", "WY")
    # )
    stateChoices = (
        ("AL", "Alabama"), ("AK", "Alaska"), ("AZ", "Arizona"), ("AR", "Arkansas"), ("CA", "California"),
        ("CO", "Colorado"), ("CT", "Connecticut"), ("DC", "Washington DC"), ("DE", "Delaware"), ("FL", "Florida"),
        ("GA", "Georgia"), ("GU", "Guam"), ("HI", "Hawaii"), ("ID", "Idaho"), ("IL", "Illinois"), ("IN", "Indiana"),
        ("IA", "Iowa"), ("KS", "Kansas"), ("KY", "Kentucky"), ("LA", "Louisiana"), ("ME", "Maine"), ("MD", "Maryland"),
        ("MA", "Massachusetts"), ("MI", "Michigan"), ("MN", "Minnesota"), ("MS", "Mississippi"), ("MO", "Missouri"),
        ("MT", "Montana"), ("NE", "Nebraska"), ("NV", "Nevada"), ("NH", "New Hampshire"), ("NJ", "New Jersey"),
        ("NM", "New Mexico"), ("NY", "New York"), ("NC", "North Carolina"), ("ND", "North Dakota"), ("OH", "Ohio"),
        ("OK", "Oklahoma"), ("OR", "Oregon"), ("PA", "Pennsylvania"), ("PR", "Puerto Rico"), ("RI", "Rhode Island"),
        ("SC", "South Carolina"), ("SD", "South Dakota"), ("TN", "Tennessee"), ("TX", "Texas"), ("UT", "Utah"),
        ("VT", "Vermont"), ("VA", "Virginia"), ("VI", "Virgin Islands"), ("WA", "Washington"), ("WV", "West Virginia"),
        ("WI", "Wisconsin"), ("WY", "Wyoming")
    )
