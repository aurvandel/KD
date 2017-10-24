from django.conf.urls import url
from WebApp import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^templates\$',views.new_project,name = 'new_project'),
    url(r'^templates\$',views.cast,name = 'cast'),
    url(r'^templates\$',views.cast_insert,name = 'cast_insert'),
    url(r'^templates\$',views.footings_insert,name = 'footings_insert'),
    url(r'^templates\$',views.footings_table,name = 'footings_table'),
    url(r'^general_conditions\$',views.general_conditions,name = 'general_conditions'),
    url(r'^templates\$',views.slab_deck,name = 'slab_deck'),
    url(r'^templates\$',views.slab_deck_insert,name = 'slab_deck_insert'),
    url(r'^templates\$',views.slab_grade,name = 'slab_grade'),
    url(r'^templates\$',views.slab_grade_insert,name = 'slab_grade_insert'),
    url(r'^templates\$',views.waste,name = 'waste'),
    url(r'^templates\$',views.waste_insert,name = 'waste_insert'),
    url(r'^templates\$',views.projects,name = 'projects'),
    url(r'^templates\$',views.reports,name = 'reports'),
    url(r'^templates\$',views.admin,name = 'admin'),
    url(r'^templates\$',views.proposals,name = 'proposals'),
    url(r'^templates\$',views.tilt_up,name = 'tilt_up'),
]
