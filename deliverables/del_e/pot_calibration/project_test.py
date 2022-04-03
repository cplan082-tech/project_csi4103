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
i = 2

while True:
    input("start test")
    data_coms = dc.data_collection('/dev/ttyACM0',
                                   './datasets/'+csv_name+f'_{i}.csv',
                                   ['Shoulder', 'Elbow'])
    time.sleep(2) # Gives time for data_coms to initialise
    
    bg.park()
    time.sleep(1)
    
    GPIO.output(arduino_int0_trig_pin, True)
    # bg.test_pattern(both=True) # hysteresis correcton test call
    bg.plot_file("circle.json")
    GPIO.output(arduino_int0_trig_pin, False)
    data_coms.stop_listening()
    
    bg.park()
    i+=1
    
   