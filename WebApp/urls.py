from django.conf.urls import url,include
from WebApp import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login\$', auth_views.login, name='user_login'),
    url(r'^$',views.index, name = 'index'),
    url(r'^analytics\$', views.analytics, name='analytics'),
    url(r'^main_screen\$', views.main_screen, name='main_screen'),
    url(r'^budgets\$', views.budget_list, name='budgets'),
    url(r'^new_budget/(?P<pk>\d+)$', views.new_budget, name='new_budget'),
    url(r'^new_budget_footings\$', views.footings_list, name='new_budget_footings'),
    url(r'^new_budget_general_conditions\$', views.new_budget_general_conditions, name='new_budget_general_conditions'),
    url(r'^reports\$', views.reports, name='reports'),
    url(r'^services\$', views.services, name='services'),
    url(r'^new_budget_cip\$', views.cast_in_place, name='new_budget_cip'),
    url(r'^new_budget_insert_footing\$', views.new_budget_insert_footing, name='new_budget_insert_footing'),
    url(r'^new_budget_information_page\$', views.new_budget_information_page, name='new_budget_information_page'),
    url(r'^new_budget_sod\$', views.slab_on_deck_list, name='new_budget_sod'),
    url(r'^new_budget_sog\$', views.slab_on_grade_list, name='new_budget_sog'),
    url(r'^new_budget_tiltup\$', views.tilt_up_panel_list, name='new_budget_tiltup'),
    url(r'^new_budget_waste-casting\$', views.new_budget_waste_casting, name='new_budget_waste-casting'),
    url(r'^services_g_maps\$', views.services_g_maps, name='services_g_maps'),
    url(r'^services_satellite_view\$', views.services_satellite_view, name='services_satellite_view'),
    # allows budgets to be hyperlinked
    # (?P<pk>\d+) regex to pass primary key into dynamic url
    url(r'^budget/edit/(?P<pk>\d+)$', views.budget_update, name='budget_edit'),
    url(r'budget/(?P<pk>\d+)$', views.BudgetView.as_view(), name='budget-detail'),
    url(r'^footing/edit/(?P<pk>\d+)$', views.footing_update, name='footing_edit'),
    url(r'^footing/delete/(?P<pk>\d+)$', views.footing_delete, name='footing_delete'),
    url(r'^general_conditions/edit/(?P<pk>\d+)$', views.general_conditions_update, name='general_conditions_edit'),
]
