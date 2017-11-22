#TODO convert everything but BudgetView back to functions

from django.shortcuts import render, redirect
from .models import openBudgets
from django.views import generic
from .forms import *
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

class BudgetView(generic.DetailView):
    model = openBudgets

def cast_in_place(request):
    cip = castInPlace.objects.all()
    data = {}
    data['lstCastInPlace'] = cip
    return render(request, 'new_budget_cip.html', data)

def footings_list(request):
    footing = footings.objects.all()
    data = {}
    data['lstFootings'] = footing
    return render(request, 'new_budget_footings.html', data)

def footing_update(request, pk):
    footing = get_object_or_404(footings, pk = pk)
    form = NewFootingForm(request.POST or None, instance = footing)
    if form.is_valid():
        form.clean()
        form.save(commit=True)
        return redirect('footings_list')
    return render(request, 'new_budget_insert_footing.html', {'form':form})

class SlabOnGradeView(generic.ListView): #see previous example. Class replaced old view function.
    model = slabOnGrade
    context_object_name = 'lstSlabOnGrade'
    queryset= model.objects.all().order_by('id')
    template_name = 'new_budget_sog.html'

class SlabOnDeckView(generic.ListView):
    model = slabOnDeck
    context_object_name = 'lstSlabOnDeck'
    queryset = model.objects.all().order_by('id')
    template_name = 'new_budget_sod.html'

class TiltUpPanelView(generic.ListView):
    model = tiltUp
    context_object_name = 'lstSlabOnDeck'
    queryset = model.objects.all().order_by('id')
    template_name = 'new_budget_tiltup.html'
    
def index(request):
    return render(request,"index.html")

def user_login(request):
    return render(request,"login.html")

def analytics(request):
    return render(request, "analytics.html")

def new_budget(request, pk):
    return render(request, "new_budget.html")

def new_budget_general_conditions(request):
    return render(request, "new_budget_general_conditions.html")

def reports(request):
    return render(request, "reports.html")

def services(request):
    return render(request, "services.html")

def main_screen(request):
    budgets = openBudgets.objects.all().order_by('-created')[:10]   # only show the 10 most recently created budgets
    data = {}
    data['recentBudgets'] = budgets
    return render(request, 'main_screen.html', data)

def budget_list(request):
    budgets = openBudgets.objects.all()
    data = {}
    data['object_list'] = budgets
    return render(request, 'budgets.html', data)

def budget_update(request, pk):
    budget = get_object_or_404(openBudgets, pk = pk)
    form = NewBudgetForm(request.POST or None, instance = budget)
    if form.is_valid():
        form.clean()
        form.save(commit=True)
        return redirect('budgets')
    return render(request, 'new_budget_information_page.html', {'form':form})

def new_budget_insert_footing(request):
    form = NewFootingForm()
    if request.method == 'POST':
        form = NewFootingForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save(commit=True)
            return redirect('new_budget_footings')
    return render(request, "new_budget_insert_footing.html", {'form':form})

def new_budget_information_page(request):
    form = NewBudgetForm()
    if request.method == 'POST':
        form = NewBudgetForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save(commit=True)
            return redirect('new_budget')
    return render(request, "new_budget_information_page.html", {'form':form})

def new_budget_waste_casting(request):
    return render(request, "new_budget_waste-casting.html")

def services_g_maps(request):
    return render(request, "services_g_maps.html")

def services_satellite_view(request):
    return render(request, "services_satellite_view.html")
