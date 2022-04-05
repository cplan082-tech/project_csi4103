#!/usr/bin/python3
import serial
import time
import threading

class arm_angle_collection:
    def __init__(self, coms_chan='/dev/ttyACM0', baud=9600, timeout_val=5):
        self.ser = serial.Serial(coms_chan, baud, timeout=timeout_val) # establish comms connection
        
    def angle_request(self):
        # Lets program know that a data comms error occured
        flag = False  # false when error occurs and true when no error occurs
        while(not(flag)):
            try:
                self.ser.reset_input_buffer()
                # initiates a data transfer between Arduino and RPi
                msg_b = bytes("Status", 'utf-8') # taken from lab 6
                self.ser.write(msg_b + b'\n') # taken from lab 6
                self.shoulder = int(self.ser.readline().decode("utf-8").strip())
                self.elbow = int(self.ser.readline().decode("utf-8").strip())
                flag = True # Lets program know that no data comms errors occured
                
            except:
                flag = False # Lets program know that a data comms error occured
                print("comms error detected!")
                time.sleep(0.5) # Slows data flow to prevent further lock ups.
        
        return self.shoulder, self.elbow
        
