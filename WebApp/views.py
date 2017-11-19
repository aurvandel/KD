from django.shortcuts import render
from .models import *
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


class MainScreenView(generic.ListView):     # main_screen is now a class
    model = openBudgets                     # data to populate in main_screen is from openBudgets table
    context_object_name = 'recentBudgets'   # list of fields used to tag html
    queryset = model.objects.all().order_by('-created')[:10]      # only show the 10 most recently created budgets
    template_name = 'main_screen.html'      # template to load

class BudgetsView(generic.ListView):
    model = openBudgets
    context_object_name = 'allBudgets'
    queryset = openBudgets.objects.all().order_by('-budget_id')
    template_name = 'budgets.html'

class EditBudgetView(generic.DetailView):   # allows budgets to by hyperlinked
    model = openBudgets

class CastInPlaceView(generic.ListView): # Cast in place turned into a class
    model = openBudgets.castInPlace     #data to populate in cip table
    context_object_name = 'lstCastInPlace' #list of fields used to tag html
    queryset = model.objects.all().order_by('id')   #order by django generated Id
    template_name = 'new_budget_cip.html'   #template to load from templates folder

class FootingsView(generic.ListView): #see previous example. Class replaces old view function
    model = openBudgets.footings
    context_object_name = 'lstFootings'
    queryset = model.objects.all().order_by('id')
    template_name = 'new_budget_footings.html'

class SlabOnGradeView(generic.ListView): #see previous example. Class replaced old view function.
    model = openBudgets.slabOnGrade
    context_object_name = 'lstSlabOnGrade'
    queryset= model.objects.all().order_by('id')
    template_name = 'new_budget_sog.html'

class SlabOnDeckView(generic.ListView):
    model = openBudgets.slabOnDeck
    context_object_name = 'lstSlabOnDeck'
    queryset = model.objects.all().order_by('id')
    template_name = 'new_budget_sod.html'

class TiltUpPanelView(generic.ListView):
    model = openBudgets.tiltUp
    context_object_name = 'lstSlabOnDeck'
    queryset = model.objects.all().order_by('id')
    template_name = 'new_budget_tiltup.html'
    
def index(request):
    return render(request,"index.html")

def user_login(request):
    return render(request,"login.html")

def analytics(request):
    return render(request, "analytics.html")

def new_budget(request):
    return render(request, "new_budget.html")

#def new_budget_footings(request):
#    return render(request, "new_budget_footings.html")

def new_budget_general_conditions(request):
    return render(request, "new_budget_general_conditions.html")

def reports(request):
    return render(request, "reports.html")

def services(request):
    return render(request, "services.html")

def new_budget_insert_footing(request):
    return render(request, "new_budget_insert_footing.html")

#def new_budget_sod(request):
#    return render(request, "new_budget_sod.html")

#def new_budget_sog(request):
#    return render(request, "new_budget_sog.html")

def new_budget_waste_casting(request):
    return render(request, "new_budget_waste-casting.html")

def services_g_maps(request):
    return render(request, "services_g_maps.html")

def services_satellite_view(request):
    return render(request, "services_satellite_view.html")
