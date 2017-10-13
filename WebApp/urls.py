from django.conf.urls import url
from WebApp import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
]
