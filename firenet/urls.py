from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('temperatures/', TemperatureListCreateAPIView.as_view(), name='temperature-list-create'),
    path('temperatures/<int:pk>/', TemperatureDetailUpdateDeleteAPIView.as_view(), name='temperature-detail-update-delete'),
]