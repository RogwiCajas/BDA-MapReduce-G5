from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from TaxiApp.models import TaxisModel
from TaxiApp.serializers import TaxisSerializer

# Create your views here.
def taxiAPI(request, id=0):
    
    # Operacion READ
    if request.method=='GET':
        viajesTaxi = TaxisModel.objects.all()
        viajesTaxi_serializer = TaxisSerializer(viajesTaxi, many=True)
        return JsonResponse(viajesTaxi_serializer.data, safe=False)
    
    # Operacion CREATE
    elif request.method=='POST':
        viajesTaxi_data = JSONParser().parse(request)
        viajesTaxi_serializer = TaxisSerializer(data=viajesTaxi_data)
        if viajesTaxi_serializer.is_valid():
            viajesTaxi_serializer.save()
            return JsonResponse("Viaje en taxi nuevo AÑADIDO correctamente!", safe=False)
        return JsonResponse("No fue posible AÑADIR el viaje en taxi, asegúrate de que todo esté correcto.", safe=False)

    # Operacion UPDATE
    elif request.method=='PUT':
        viajesTaxi_data = JSONParser().parse(request)
        viaje = TaxisModel.objects.get(ViajeId=viajesTaxi_data['uniqueKey'])
        viajesTaxi_serializer = TaxisSerializer(viaje, data=viajesTaxi_data)
        if viajesTaxi_serializer.is_valid():
            viajesTaxi_serializer.save()
            return JsonResponse("Viaje en taxi ACTUALIZADO correctamente!", safe=False)
        return JsonResponse("No fue posible ACTUALIZAR el viaje en taxi, asegúrate de que todo esté correcto.", safe=False)

    # Operacion DELETE
    elif request.method=='DELETE':
        viaje = TaxisModel.objects.get(ViajeId=id)
        viaje.delete()
        return JsonResponse("Viaje en taxi ELIMINADO correctamente!", safe=False)
