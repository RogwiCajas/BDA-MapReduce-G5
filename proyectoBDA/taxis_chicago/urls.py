from taxis_chicago.views import TaxisViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = 'taxis_chicago'


router = DefaultRouter()
router.register(r'taxis', TaxisViewSet, basename='taxis')
urlpatterns = router.urls
'''
urlpatterns  += [
    path('test/',(TaxisViewSet.as_view()),name="taxis" ),
    path('test_delete/<str:id>',(TaxisViewSet.as_view()),name="taxis" ),
]
'''
