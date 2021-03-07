import serial, numpy

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)

while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print(data)