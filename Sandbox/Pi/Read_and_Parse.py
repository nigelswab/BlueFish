import os
import serial
import time
import csv
from datetime import datetime

import csv_logger

fileName = "Testing Logging"
test_plan = '' # link to word test_plan on onedrive
test_notes = '' # anything of note for this test
firmware = '' #to keep track of updates -> use firmware id in git commits so revision can be returned to if needed
#tuning_parameters = '' #PID variable levels (ki kp etc)

log= csv_logger.Logger(fileName, test_plan, test_notes, firmware)

# set usb port name, naud rate, and timeout so program doesn't get stuck
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=.1)

# get rid of garbage/incomplete data
arduino.flush()

# Infinite loop
while True:
    
        # Read until new line char and convert byte data into string, and log into csv
        line = arduino.readline().decode('utf-8').rstrip()
        log.log_row(line)
        print(line)
    
          
        
