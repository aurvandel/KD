from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
	return render(request,"index.html")

def user_login(request):
	return render(request,"login.html")

def analytics(request):
	return render(request, "analytics.html")

def budgets(request):
	return render(request, "budgets.html")

def main_screen(request):
	return render(request, "main_screen.html")

def new_budget(request):
	return render(request, "new_budget.html")

def new_budget_footings(request):
	return render(request, "new_budget_footings.html")

def new_budget_general_conditions(request):
	return render(request, "new_budget_general_conditions.html")

def reports(request):
	return render(request, "reports.html")

def services(request):
	return render(request, "services.html")