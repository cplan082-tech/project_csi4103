import time
import RPi.GPIO as GPIO
from custom import bg


while True:
    input("start test")
    
    bg.park()
    time.sleep(1)
    bg.plot_file("arc.json")
#    bg.test_pattern(reverse=True)
    bg.park()
    
