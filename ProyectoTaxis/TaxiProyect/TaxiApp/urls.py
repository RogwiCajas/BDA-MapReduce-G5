from django.conf import urls
from django.conf.urls import url
from TaxiApp import views

#Se añaden las vistas CRUD
urlpatterns = [
    url(r'^taxis$', views.taxiAPI),
    url(r'^taxis/\"([a-z0-9]+\")$', views.taxiAPI)
]