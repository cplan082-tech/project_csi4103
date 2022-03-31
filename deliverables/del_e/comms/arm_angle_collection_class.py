#!/usr/bin/python3
import serial
import time
import threading

class arm_angle_collection:
    def __init__(self, coms_chan='/dev/ttyACM0', baud=9600, timeout_val=5):
        self.ser = serial.Serial(coms_chan, baud, timeout=timeout_val) # establish comms connection
        
    def angle_request(self):
        self.ser.reset_input_buffer()
        msg_b = bytes("Status", 'utf-8')
        ser.write(msg_b)
        self.shoulder = int(ser.readline().decode("utf-8").strip())
        self.elbow = int(ser.readline().decode("utf-8").strip())
        
        return self.shoulder, self.elbow
        