# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 22:35:23 2022

@author: clive
"""

# import os
# import sys

# sys.path.append(os.path.realpath('../../../base_project'))

# from BrachioGraphError import BrachioGraphError
import time
import RPi.GPIO as GPIO
import data_collection_class as dc
from custom import bg
arduino_int0_trig_pin = 40


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(arduino_int0_trig_pin, GPIO.OUT)
GPIO.output(arduino_int0_trig_pin, False)

csv_name = 'hyster_dataset_clean'
i = 4

while True:
#     input("Press enter to establish communications")
    data_coms = dc.data_collection('/dev/ttyACM0',
                                   './datasets/'+csv_name+f'_{i}.csv',
                                   ['Shoulder', 'Elbow'])
#     time.sleep(3) # Gives time for data_coms to initialise
    
    print("putting pen down")
    bg.pen.down()
    time.sleep(1)
    
    input("Press enter to start test")
    GPIO.output(arduino_int0_trig_pin, True)
    input("Press enter to stop test")
    data_coms.stop_listening()
    GPIO.output(arduino_int0_trig_pin, False)
    print("Test completed. data ready to be pushed")
    i+=1