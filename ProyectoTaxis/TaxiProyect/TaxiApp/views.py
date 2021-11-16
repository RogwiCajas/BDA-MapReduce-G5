from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from TaxiApp.models import TaxisModel
from TaxiApp.serializers import TaxisSerializar
# Create your views here.

#aqui van las view del crud 