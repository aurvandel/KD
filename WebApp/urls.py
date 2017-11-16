from django.conf.urls import url,include
from WebApp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login\$', auth_views.login, name='user_login'),
    url(r'^$',views.index, name = 'index'),
    url(r'^analytics\$', views.analytics, name='analytics'),
    url(r'^budgets\$', views.budgets, name='budgets'),
    url(r'^main_screen\$', views.main_screen, name='main_screen'),
    url(r'^new_budget\$', views.new_budget, name='new_budget'),
    url(r'^new_budget_footings\$', views.new_budget_footings, name='new_budgets_footings'),
    url(r'^new_budget_general_conditions\$', views.new_budget_general_conditions, name='new_budget_general_conditions'),
    url(r'^reports\$', views.reports, name='reports'),
    url(r'^services\$', views.services, name='services'),
]
