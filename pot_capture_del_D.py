import data_collection_class as dc

csv_name = 'pot_capture_dataset'
i = 1

while True:
    input("Press any key to start test")
    
    data_coms = dc.data_collection('/dev/ttyUSB0',
                                   './datasets/'+csv_name+f'_{i}.csv',
                                   ['pot_val', 'digital_val'])
    print("Initializing data comms channel")
    time.sleep(3) # Gives time for data_coms to initialise
    
    print("test running")
    
    input("Press any key to stop test")    
    data_coms.stop_listening()

    
    print("Test terminated**************************")
    
    
    i+=1