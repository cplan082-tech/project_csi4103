# import os
# import sys

# sys.path.append(os.path.realpath('../../../base_project'))

# from BrachioGraphError import BrachioGraphError
import time
from custom import bg

# bg = BrachioGraphError(
#     servo_1_parked_pw=1475,
#     servo_2_parked_pw=1350)


bg.park()
time.sleep(1)

#bg.box(bounds=[-6, 11, 6, 20]) # largest rectangle at center, hypotenuse = 15.620
bg.test_pattern(both=True) # hysteresis correcton test call

time.sleep(1)
bg.park()

# bg.plot_file("circle.json")
