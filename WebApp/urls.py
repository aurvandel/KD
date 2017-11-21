from django.conf.urls import url,include
from WebApp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login\$', auth_views.login, name='user_login'),
    url(r'^$',views.index, name = 'index'),
    url(r'^analytics\$', views.analytics, name='analytics'),
    #url(r'^budgets\$', views.budgets, name='budgets'),
    # changed code for main_screen, budgets because it's importing a class not a function
    url(r'^main_screen\$', views.MainScreenView.as_view(), name='main_screen'),
    url(r'^budgets\$', views.BudgetsView.as_view(), name='budgets'),
    url(r'^new_budget\$', views.new_budget, name='new_budget'),
    url(r'^new_budget_footings\$', views.FootingsView.as_view(), name='new_budget_footings'),
    url(r'^new_budget_general_conditions\$', views.new_budget_general_conditions, name='new_budget_general_conditions'),
    url(r'^reports\$', views.reports, name='reports'),
    url(r'^services\$', views.services, name='services'),
    url(r'^new_budget_cip\$', views.CastInPlaceView.as_view(), name='new_budget_cip'),
    url(r'^new_budget_insert_footing\$', views.new_budget_insert_footing, name='new_budget_insert_footing'),
    url(r'^new_budget_information_page\$', views.new_budget_information_page, name='new_budget_information_page'),
    url(r'^new_budget_sod\$', views.SlabOnDeckView.as_view(), name='new_budget_sod'),
    url(r'^new_budget_sog\$', views.SlabOnGradeView.as_view(), name='new_budget_sog'),
    url(r'^new_budget_tiltup\$', views.TiltUpPanelView.as_view(), name='new_budget_tiltup'),
    url(r'^new_budget_waste-casting\$', views.new_budget_waste_casting, name='new_budget_waste-casting'),
    url(r'^services_g_maps\$', views.services_g_maps, name='services_g_maps'),
    url(r'^services_satellite_view\$', views.services_satellite_view, name='services_satellite_view'),
    # allows budgets to be hyperlinked
    url(r'^budget/(?P<pk>\d+)$', views.EditBudgetView.as_view(), name='budget-detail'),
]
