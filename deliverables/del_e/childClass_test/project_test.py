# import os
# import sys

# sys.path.append(os.path.realpath('../../../base_project'))

# from BrachioGraphError import BrachioGraphError
import time
from custom import bg

# bg = BrachioGraphError(
#     servo_1_parked_pw=1475,
#     servo_2_parked_pw=1350)


bg.set_angles(-90,80)
time.sleep(3)

bg.park()

# bg.plot_file("circle.json")
