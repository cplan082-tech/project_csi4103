# import os
# import sys

# sys.path.append(os.path.realpath('../../../base_project'))

# from BrachioGraphError import BrachioGraphError
import time
import RPi.GPIO as GPIO
import data_collection_class as dc
from custom import bg
arduino_int0_trig_pin = 4


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(arduino_int0_trig_pin, GPIO.OUT)
GPIO.output(arduino_int0_trig_pin, False)

csv_name = 'hyster_dataset_clean'
i = 1

while True:
    input("start test")
    data_coms = dc.data_collection('/dev/ttyACM0',
                                   './datasets/'+csv_name+f'_{i}.csv',
                                   ['Shoulder', 'Elbow'])
    time.sleep(2) # Gives time for data_coms to initialise
    
    bg.park()
    time.sleep(1)
    input("Press enter to fully extend the arm to the left")
    
    bg.set_angles(0, -90)
    time.sleep(1)
    print("Press push button to take measurments")
    
    GPIO.output(arduino_int0_trig_pin, True)
    bg.test_pattern(both=True) # hysteresis correcton test call
    GPIO.output(arduino_int0_trig_pin, False)
    data_coms.stop_listening()
    
    bg.park()
    i+=1
    
    # bg.plot_file("circle.json")
