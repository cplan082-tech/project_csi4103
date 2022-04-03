# import os
# import sys

# sys.path.append(os.path.realpath('../../../base_project'))

import time
import RPi.GPIO as GPIO
import data_collection_class as dc
from custom import bg
arduino_int0_trig_pin = 40


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(arduino_int0_trig_pin, GPIO.OUT)
GPIO.output(arduino_int0_trig_pin, False)


arduino_int0_trig_pin = 40
bg.park()
GPIO.output(arduino_int0_trig_pin, False)
print("Park complete")


# bg.plot_file("circle.json")
