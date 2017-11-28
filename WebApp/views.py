from django.shortcuts import render, redirect
from .models import *
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
        return redirect('new_budget_footings')
    return render(request, 'new_budget_insert_footing.html', {'form':form})

def new_budget_insert_footing(request):
    form = NewFootingForm()
    if request.method == 'POST':
        form = NewFootingForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save(commit=True)
            return redirect('new_budget_footings')
    return render(request, "new_budget_insert_footing.html", {'form':form})

def new_budget_general_conditions(request):
    gc = GeneralConditions.objects.all()
    form = NewGeneralConditionForm()
    if request.method == 'POST':
        form = NewGeneralConditionForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save(commit=True)
            return redirect('new_budget_general_conditions')
    return render(request, 'new_budget_general_conditions.html', {'lstgc':gc, 'form':form})

def general_conditions_update(request, pk):
    gc = GeneralConditions.objects.all()
    generalCondition = get_object_or_404(GeneralConditions, pk = pk)
    form = NewGeneralConditionForm(request.POST or None, instance = generalCondition)
    if form.is_valid():
        form.clean()
        form.save(commit=True)
        return redirect('new_budget_general_conditions')
    return render(request, 'new_budget_general_conditions_update.html', {'form':form, 'lstgc':gc})

def general_conditions_delete(request, pk):
    lstgc = GeneralConditions.objects.all()
    gc = get_object_or_404(GeneralConditions, pk=pk)
    if request.method=='POST':
        gc.delete()
        return redirect('new_budget_general_conditions')
    return render(request, 'general_conditions_confirm_delete.html', {'object':gc, 'lstFootings':lstgc})

def footing_delete(request, pk):
    lstFootings = footings.objects.all()
    footing = get_object_or_404(footings, pk=pk)
    if request.method=='POST':
        footing.delete()
        return redirect('new_budget_footings')
    return render(request, 'footing_confirm_delete.html', {'object':footing, 'lstFootings':lstFootings})

def slab_on_grade_list(request):
    slab = slabOnGrade.objects.all()
    data = {}
    data['lstSlabOnGrade'] = slab
    return render(request, 'new_budget_sog.html', data)

def slab_on_deck_list(request):
    slab = slabOnDeck.objects.all()
    data = {}
    data['lstSlabOnDeck'] = slab
    return render(request, 'new_budget_sod.html', data)

def tilt_up_panel_list(request):
    panel = tiltUp.objects.all()
    data = {}
    data['lstTiltUp'] = panel
    return render(request, 'new_budget_tiltup.html', data)
    
def index(request):
    return render(request,"index.html")

def user_login(request):
    return render(request,"login.html")

def analytics(request):
    return render(request, "analytics.html")

def new_budget(request, pk):
    return render(request, "new_budget.html")

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
    wc = WasteCasting.objects.all()
    data = {}
    data['lstwc'] = wc
    return render(request, 'new_budget_waste-casting.html', data)

def services_g_maps(request):
    return render(request, "services_g_maps.html")

def services_satellite_view(request):
    return render(request, "services_satellite_view.html")

