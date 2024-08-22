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

from rest_framework import generics
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataCreateView(generics.CreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer

# from rest_framework import viewsets
# from rest_framework.response import Response
# from .models import SensorData
# from .serializers import SensorDataSerializer
# class SensorDataViewSet(viewsets.ViewSet):
#     def list(self, request):
#         # Get the latest sensor data record
#         latest_sensor_data = SensorData.objects.order_by('-created_at').first()
#         if latest_sensor_data:
#             serializer = SensorDataSerializer(latest_sensor_data)
#             return Response(serializer.data)
#         else:
#             return Response(status=404)

from rest_framework import viewsets
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer
import joblib
class SensorDataViewSet(viewsets.ViewSet):
    def list(self, request):
        # Load the trained model from the pkl file
        clf = joblib.load('/home/ashish/FInal_Year_Project_Backend/Firenet_backend/firenet/scripts/trained_model3.pkl')

        # Get the latest sensor data record
        latest_sensor_data = SensorData.objects.order_by('-created_at').first()
        if latest_sensor_data:
            # Extract temperature and humidity values from the latest sensor data
            temperature = latest_sensor_data.temperature
            humidity = latest_sensor_data.humidity

            # Use the trained ML model to predict fire status
            prediction = clf.predict([[temperature, humidity]])
            print(prediction)

            # Serialize the latest sensor data
            serializer = SensorDataSerializer(latest_sensor_data)

            # Include the prediction in the response data
            response_data = {
                'temperature': temperature,
                'humidity': humidity,
                'fire_prediction': bool(prediction),
                'sensor_data': serializer.data
            }

            return Response(response_data)
        else:
            return Response(status=404)

# views.py
from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorDataSerializer

class AllSensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all()
    serializer_class = SensorDataSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid credentials'}, status=HTTP_400_BAD_REQUEST)

        login(request, user)  # Log the user in
        return Response({'message': 'Login successful'}, status=HTTP_200_OK)


# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client

@api_view(['POST'])
def stop_alert(request):
    if request.method == 'POST':
        # account_sid = "REDACTED"
        # auth_token =
        # twilio_number =
        # phone_numbers =
        # message_content = "ALERT: FIRE DETECTED IN YOUR AREA!"

        client = Client(account_sid, auth_token)

        # Send SMS messages to each phone number
        for phone_number in phone_numbers:
            message = client.messages.create(
                body=message_content,
                from_=twilio_number,
                to=phone_number
            )
            print(f"Message sent to {phone_number}: {message.sid}")

        return Response({'message': 'Alert stopped and messages sent'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Only POST requests are allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




    