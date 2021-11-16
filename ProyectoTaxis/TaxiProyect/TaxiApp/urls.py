from django.conf.urls import url
from django.urls.resolvers import URLPattern
from TaxiApp import views

#Se añaden las vistas CRUD
urlpatterns = [
    url(r'ver/', views.taxiAPI),
    url(r'borrar/<str:id>', views.taxiAPI),
    #url(r'^viajeentaxi/([0-9]+)$',)
]