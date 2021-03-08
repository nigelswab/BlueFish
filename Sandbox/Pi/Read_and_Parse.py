import serial
import time
import csv

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)
arduino.flushInput()

while True:
    try:
        arduino_bytes = arduino.readline()
        decoded_bytes = (arduino_bytes[0:len(arduino_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        
    except:
        print("Error: Keyboard Interrupt")
        break   
        
