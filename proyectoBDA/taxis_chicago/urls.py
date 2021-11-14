from taxis_chicago.views import TaxisViewSet
from rest_framework.routers import DefaultRouter


app_name = 'taxis_chicago'


router = DefaultRouter()
router.register(r'taxis', TaxisViewSet, basename='taxis')
urlpatterns = router.urls