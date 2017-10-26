from django.conf.urls import url
from WebApp import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'^new_project\$',views.new_project,name = 'new_project'),
    url(r'^cast\$',views.cast,name = 'cast'),
    url(r'^cast_insert\$',views.cast_insert,name = 'cast_insert'),
    url(r'^footings_insert\$',views.footings_insert,name = 'footings_insert'),
    url(r'^footings_table\$',views.footings_table,name = 'footings_table'),
    url(r'^general_conditions\$',views.general_conditions,name = 'general_conditions'),
    url(r'^slab_deck\$',views.slab_deck,name = 'slab_deck'),
    url(r'^slab_deck_insert\$',views.slab_deck_insert,name = 'slab_deck_insert'),
    url(r'^slab_grade\$',views.slab_grade,name = 'slab_grade'),
    url(r'^slab_grade_insert\$',views.slab_grade_insert,name = 'slab_grade_insert'),
    url(r'^waste\$',views.waste,name = 'waste'),
    url(r'^waste_insert\$',views.waste_insert,name = 'waste_insert'),
    url(r'^projects\$',views.projects,name = 'projects'),
    url(r'^reports\$',views.reports,name = 'reports'),
    url(r'^admin\$',views.admin,name = 'admin'),
    url(r'^proposals\$',views.proposals,name = 'proposals'),
    url(r'^tilt_up\$',views.tilt_up,name = 'tilt_up'),
]
