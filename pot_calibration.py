# runn <sudo pigpiod> in shell first
import os
import sys

sys.path.append(os.path.realpath('./base_project'))

from brachiograph import BrachioGraph
import data_collection_class as dc
import time
import RPi.GPIO as gpio

# interupt on Arduino vvvvvvvvvvvvvvv
arduino_int0_trig_pin = 16

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(arduino_int0_trig_pin, gpio.OUT)
gpio.output(arduino_int0_trig_pin, False)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

bg = BrachioGraph()

csv_name = 'pot_calibration_dataset'
i = 1

while True:
    data_coms = dc.data_collection('/dev/ttyACM0',
                                   './datasets/'+csv_name+f'_{i}.csv',
                                   ['Shoulder Angle', 'Elbow Angle'])
    print("Initializing data comms channel")
    time.sleep(3) # Gives time for data_coms to initialise

    print("Set shoulder limb to -90 degrees and elbow to 90 degrees. Make sure elbow is not connected")
    input("Press any key to move shoulder limb")
    bg.park()


    print("Attach elbow limb to make 90 degree angle with shoulder and elbow.")
    print("******************************************************************")
    print("\n")

    print("Take reading for full arm extension")
    input("Press any key to start")

    bg.set_angles(-90, 0)
    print("Letting arm settle")
    time.sleep(2)
    gpio.output(arduino_int0_trig_pin, True)
    print("taking measurment")
    time.sleep(1)
    gpio.output(arduino_int0_trig_pin, False)
    print("Measurment taken")
    print("******************************************************************")
    print("\n")
    
    print("Take reading for elbow fully extended inwards.")
    print("Be carefull on this one. Could cause are to break itself")
    print("Elbow Angle presently set to 145 degrees")
    input("Press any key to start")
    bg.set_angles(-90, 145)
    
    print("Letting arm settle")
    time.sleep(2)
    gpio.output(arduino_int0_trig_pin, True)
    print("taking measurment")
    time.sleep(1)
    gpio.output(arduino_int0_trig_pin, False)
    print("Measurment taken")
    print("******************************************************************")
    print("\n")
    
    print("Take reading for shoulder fully extended inwards.")
    input("Press any key to start")
    print("Voving back to home position")
    bg.park()
    print("Letting arm settle")
    time.sleep(2)
    print("Fully extending elbow")
    bg.set_angles(-90, 0)
    print("Letting arm settle")
    time.sleep(2)
    print("Fully extending shoulder")
    bg.set_angles(90, 0)
    
    print("Letting arm settle")
    time.sleep(2)
    gpio.output(arduino_int0_trig_pin, True)
    print("taking measurment")
    time.sleep(1)
    gpio.output(arduino_int0_trig_pin, False)
    print("Measurment taken")
    print("******************************************************************")
    print("\n")
    data_coms.stop_listening()
    
