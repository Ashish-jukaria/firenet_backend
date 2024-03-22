from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Temperature
from rest_framework import generics
from .models import Temperature
from .serializers import Temperature_Serializers

class TemperatureListCreateAPIView(generics.ListCreateAPIView):
    queryset = Temperature.objects.all()
    serializer_class = Temperature_Serializers

class TemperatureDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Temperature.objects.all()
    serializer_class = Temperature_Serializers

class HelloWorldView(APIView):
    def get(self, request, format=None):
        data = {'message': 'Hello, world!'}
        return Response(data)


    