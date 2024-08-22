import serial
import requests
import time

# Configure the serial port and baud rate
SERIAL_PORT = '/dev/ttyACM0'  # Replace with your Arduino's serial port
BAUD_RATE = 9600

# Django API endpoint
API_ENDPOINT = 'http://localhost:8000/api/sensor-data/'  # Replace with your API endpoint

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

while True:
    try:
        # Read data from Arduino
        line = ser.readline().decode('utf-8').strip()
        print(f"Received data: {line}")

        # Split the data into temperature and humidity
        temperature, humidity = map(float, line.split(','))

        # Prepare data for API request
        payload = {
            'temperature': temperature,
            'humidity': humidity
        }

        # Send data to Django API
        response = requests.post(API_ENDPOINT, json=payload)
        print(f"API response: {response.status_code} - {response.text}")

        # Wait before the next reading
        time.sleep(1)  # Adjust delay as needed

    except Exception as e:
        print(f"Error: {e}")
