from django.shortcuts import render

from rest_framework.exceptions import NotFound

from taxis_chicago.firebase_client import FirebaseClient
from taxis_chicago.serializers import TaxisSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class TaxisViewSet(viewsets.ViewSet):
    client = FirebaseClient()

    def create(self, request, *args, **kwargs):
        serializer = TaxisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.create(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def list(self, request):
        todos = self.client.all()
        serializer = TaxisSerializer(todos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo = self.client.get_by_id(pk)

        if todo:
            serializer = TaxisSerializer(todo)
            return Response(serializer.data)

        raise NotFound(detail="Todo Not Found", code=404)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.client.delete_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = TaxisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.update(pk, serializer.data)

        return Response(serializer.data)
