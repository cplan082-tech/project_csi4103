# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:55:30 2022

@author: clive
"""
# import os
# import sys

# sys.path.append(os.path.realpath('../../../base_project'))
# from BrachioGraphError import BrachioGraphError

# bg = BrachioGraphError(
#     servo_1_parked_pw=1475,
#     servo_2_parked_pw=1350)


import os
import sys

sys.path.append(os.path.realpath('../../../base_project'))

from brachiograph import BrachioGraph
bg = BrachioGraph(
    inner_arm=10,
    outer_arm=11,
    bounds=[-5, 10, 5, 20],
    servo_1_parked_pw=1525,
    servo_2_parked_pw=1500,
    hysteresis_correction_1=12,
    hysteresis_correction_2=12)
