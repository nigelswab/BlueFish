import serial
import time
import csv

# set usb port name, naud rate, and timeout so program doesn't get stuck
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)

# get rid of garbage/incomplete data
arduino.flush()

# create a firle name and open to be appended 
fileName="serial-test.csv" 
file = open(fileName, "a")
print(fileName + " created")

# Infinite loop
while True:
    try:
        # Read until new line char and convert byte data into string,
        # removing trailing chars like new line '\n'
        line = arduino.readline().decode('utf-8').rstrip()
        print(line)
        
        
        #append the data to the file
        file = open(fileName, "a")
        #write data with a new line
        file.write(line + "\\n") 
        
        

    except:
        #close out the file
        file.close()
        
        print("Error: Keyboard Interrupt")
        break   
        
