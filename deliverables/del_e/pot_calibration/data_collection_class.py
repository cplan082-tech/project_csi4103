import serial
import RPi.GPIO as gpio
import time
import pandas as pd
import threading
import sys
import numpy as np

class data_collection:
    def __init__(self, coms_chan, ouput_csv, cols, ser_delay=3):
        self.ser_delay = ser_delay
        self.ouput_csv = ouput_csv # name of output csv file
        time.sleep(1) # prevents serial connection from reading "" when called repetedly
        self.ser = serial.Serial(coms_chan, 9600, timeout=30) # establish comms connection
        self.lock = threading.Lock() # Create thread locking object
        self.cols = cols
        self.df = pd.DataFrame(columns=cols) # creates empty dataframe
        print("\n")
        print('starting comms thread, please wait')
#         self.ser.reset_input_buffer() # resets input buffer before starting thread
        self.running = True # used to enable or disable the thread (when True, loops to infinity)
        self.listen_thread = threading.Thread(target=self.waiting_for_data)
        self.listen_thread.start() # starts thread
        for _ in range(30):
            sys.stdout.write(".")
            sys.stdout.flush()
#             print(".")
            time.sleep(self.ser_delay/30)
        print("\nComms thread started")
        print("\n")
        
    def pack_data(self):
        self.lock.acquire() # prevents thread from terminating during data aquisition
        
        # Creates a list were the number of elements is equal to the number of columns of the df
        data = [(float(self.ser.readline().decode('utf-8').rstrip())) for _ in range(len(self.cols))]
#         print(data)
        df_temp = pd.DataFrame(np.array(data).reshape(1,-1),
                              columns=self.cols) # concats new data to dataframe
        self.df = pd.concat([self.df, df_temp]).reset_index(drop=True)            
        self.lock.release()
    
    # method used by thread
    def waiting_for_data(self):
        self.ser.reset_input_buffer() # resets input buffer before starting thread
        while self.running: # runs while self.running = True
            if (self.ser.in_waiting > 0): # if serial input buffer has data, trigger pack_data() method
                self.pack_data()
    
    # method is called by user when comms are to be terminated and collected
    # data converted to csv
    def stop_listening(self):
        self.lock.acquire() # prevents new data from coming in while converting data to csv
        self.df.to_csv(self.ouput_csv, index=False) # converts dataframe to csv
        print('data converted to csv')
        self.running = False # terminated comms thread
        print("\n")
#         print("Terminating comms thread, please wait")
        self.lock.release()
#         time.sleep(self.ser_delay)
        print('Comms thread terminated')
        print("\n")
                
                