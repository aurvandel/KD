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
    url(r'^new_budget_footings\$', views.new_budget_footings, name='new_budget_footings'),
    url(r'^new_budget_general_conditions\$', views.new_budget_general_conditions, name='new_budget_general_conditions'),
    url(r'^reports\$', views.reports, name='reports'),
    url(r'^services\$', views.services, name='services'),
    url(r'^new_budget_cip\$', views.new_budget_cip, name='new_budget_cip'),
    url(r'^new_budget_insert_footing\$', views.new_budget_insert_footing, name='new_budget_insert_footing'),
    url(r'^new_budget_sod\$', views.new_budget_sod, name='new_budget_sod'),
    url(r'^new_budget_sog\$', views.new_budget_sog, name='new_budget_sog'),
    url(r'^new_budget_waste-casting\$', views.new_budget_waste_casting, name='new_budget_waste-casting'),
    url(r'^services_g_maps\$', views.services_g_maps, name='services_g_maps'),
    url(r'^services_satallite_view\$', views.services_satallite_view, name='services_satallite_view'),
]
