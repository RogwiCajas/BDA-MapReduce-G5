from django.conf.urls import url
from django.urls.resolvers import URLPattern
from TaxiApp import views

#Se añaden las vistas CRUD
urlpatterns = [
    url(r'^viajeentaxi$', views.taxiAPI),
    url(r'^viajeentaxi/([0-9]+)$')
]