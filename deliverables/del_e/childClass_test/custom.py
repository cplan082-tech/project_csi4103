# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:55:30 2022

@author: clive
"""
from BrachioGraphError import BrachioGraphError

# bg = BrachioGraphError(
#     servo_1_parked_pw=1475,
#     servo_2_parked_pw=1350)


bg = BrachioGraphError(
    inner_arm=10,
    outer_arm=11,
    bounds=[-6, 11, 6, 20],
    servo_1_parked_pw=1525,
    servo_2_parked_pw=1500)
