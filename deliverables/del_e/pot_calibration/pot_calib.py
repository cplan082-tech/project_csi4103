# import os
# import sys

# sys.path.append(os.path.realpath('../../../base_project'))

# from BrachioGraphError import BrachioGraphError
import time
# import RPi.GPIO as GPIO
import data_collection_class as dc
#from custom import bg
csv_name = 'pot_cal_dataset_clean'
i = 2


data_coms = dc.data_collection('/dev/ttyACM0',
                               './datasets/'+csv_name+f'_{i}.csv',
                               ['Shoulder', 'Elbow'])
time.sleep(2) # Gives time for data_coms to initialise

input("Hit enter when done test")
data_coms.stop_listening()
    

