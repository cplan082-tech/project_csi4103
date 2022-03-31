import arm_angle_collection_class as arm
import time

obj_arm = arm.arm_angle_collection()

time.sleep(3)

while True:
    input("Hit enter to aquire angles")
    shoulder,elbow = obj_arm.angle_request()

    print(f'Shoulder angle ADC value: {shoulder}')
    print(f'Elbow angle ADC value: {elbow}')
    
    