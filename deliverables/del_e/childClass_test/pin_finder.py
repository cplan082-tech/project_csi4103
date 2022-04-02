# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:58:38 2022

@author: clive
"""

import RPi.GPIO as GPIO

arduino_int0_trig_pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(arduino_int0_trig_pin, GPIO.OUT)
GPIO.output(arduino_int0_trig_pin, True)