import serial
import os

# Data
channel = "COM3"
rate = 111520

ser = serial.Serial(channel, baudrate=rate, timeout=1)

while 1:
    data = ser.readline().decode()
    if data:
        data = data.split(".")
        temp = data[0]
        hum = data[1]

        os.system("cls")
        print("[Data]:")
        print("Temperature: " + temp + "c")
        print("Humidity: " + hum + "%")