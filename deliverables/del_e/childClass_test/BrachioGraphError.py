import os
import sys
import time

sys.path.append(os.path.realpath('../../../base_project'))
sys.path.append(os.path.realpath('../comms'))

import arm_angle_collection_class as arm # path might be wrong


obj_arm = arm.arm_angle_collection(coms_chan='/dev/ttyACM0')

from brachiograph import BrachioGraph

def map_func(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# houlder_min=203, soulder_max=599, elbow_min=650, elbow_max=50,
# shoulder_min_angle =-90, shoudler_max_angle=0, elbow_min_angle=0, elbow_max_angle=150

def adc2angle(lst, shoulder_min=203, soulder_max=599, elbow_min=550, elbow_max=50,
              shoulder_min_angle =-90, shoudler_max_angle=10, elbow_min_angle=0, elbow_max_angle=150):
    
    # convertes first column (shoulder) to angles between -90 and 0
    lst[0] = map_func(lst[0], shoulder_min, soulder_max, shoulder_min_angle, shoudler_max_angle)
    
    # convertes second column (elbow) to angles between 0 and 160
    lst[1] = map_func(lst[1], elbow_min, elbow_max, elbow_min_angle, elbow_max_angle)
    return lst

def proportional_controller(set_point, process_variable):
     Kp = 0.1 #proportional gain
     error = set_point - process_variable
     output = Kp * error
     return output

class BrachioGraphError(BrachioGraph):      

    def set_angles_wrapped(self, angle_1, angle_2):
        """Moves the servo motors to the specified angles immediately. Relies upon getting accurate pulse-width
        values.
        Calls set_pulse_widths().
        Sets current_x, current_y.
        """

        pw_1 = pw_2 = None

        if angle_1 is not None:
            pw_1 = self.angles_to_pw_1(angle_1)

            if pw_1 > self.previous_pw_1:
                self.active_hysteresis_correction_1 = self.hysteresis_correction_1
            elif pw_1 < self.previous_pw_1:
                self.active_hysteresis_correction_1 = - self.hysteresis_correction_1

            self.previous_pw_1 = pw_1

            pw_1 = pw_1 + self.active_hysteresis_correction_1

            self.angle_1 = angle_1
            self.angles_used_1.add(int(angle_1))
            self.pulse_widths_used_1.add(int(pw_1))

        if angle_2 is not None:
            pw_2 = self.angles_to_pw_2(angle_2)

            if pw_2 > self.previous_pw_2:
                self.active_hysteresis_correction_2 = self.hysteresis_correction_2
            elif pw_2 < self.previous_pw_2:
                self.active_hysteresis_correction_2 = - self.hysteresis_correction_2

            self.previous_pw_2 = pw_2

            pw_2 = pw_2 + self.active_hysteresis_correction_2

            self.angle_2 = angle_2
            self.angles_used_2.add(int(angle_2))
            self.pulse_widths_used_2.add(int(pw_2))

        if self.turtle:

            x, y = self.angles_to_xy(self.angle_1, self.angle_2)

            self.turtle.setx(x * self.turtle.multiplier)
            self.turtle.sety(y * self.turtle.multiplier)

        self.set_pulse_widths(pw_1, pw_2)
        self.x, self.y = self.angles_to_xy(self.angle_1, self.angle_2)

        return

    #Modified to use error correction
    def set_angles(self, angle_1=None, angle_2=None):

        shoulder_angle_anchor = angle_1
        elbow_angle_anchor = angle_2
        error_eps = 2


        # calls get_angle for the first time
        self.set_angles_wrapped(angle_1, angle_2)
        
        # get pot values
        shoulder_pot, elbow_pot = obj_arm.angle_request()

        #Convert pot ADC values to angles - THIS HAS TO BE TESTED
#         shoulder_pot = shoulder_motor_angle(shoulder_pot)
#         elbow_pot = elbow_angle(elbow_pot)
        lst_angles = adc2angle([shoulder_pot, elbow_pot])
        shoulder_pot = lst_angles[0]
        elbow_pot = lst_angles[1]
        
        # calculate error
        shoulder_error  = abs(shoulder_angle_anchor - shoulder_pot)
        elbow_error = abs(elbow_angle_anchor - elbow_pot)

        #set variables for P controller
        shoulder_angle = shoulder_angle_anchor
        elbow_angle = elbow_angle_anchor

        # determine if error is acceptable (for now, test with 1 degree error maximum)
        while (shoulder_error > error_eps or elbow_error > error_eps):
            time.sleep(0.05)

            if (shoulder_error > error_eps):
                shoulder_angle = shoulder_angle + proportional_controller(shoulder_angle_anchor,shoulder_pot)

            if (elbow_error > error_eps):
                elbow_angle = elbow_angle + proportional_controller(elbow_angle_anchor,elbow_pot)

            self.set_angles_wrapped(shoulder_angle, elbow_angle)
            
            # get pot values
            shoulder_pot, elbow_pot = obj_arm.angle_request()
            
            # convert pot ADC values to angles
            lst_angles = adc2angle([shoulder_pot, elbow_pot])
            shoulder_pot = lst_angles[0]
            elbow_pot = lst_angles[1]
            
            print(f'Shoulder angle anckor: {shoulder_angle_anchor}')
            print(f'Shoulder pot angle: {shoulder_pot}')
            print(f'Shoulder angle: {shoulder_angle}')
            print("=================================================")
            print(f'Elbow angle anckor: {elbow_angle_anchor}')
            print(f'Elbow pot angle: {elbow_pot}')
            print(f'Elbow angle: {elbow_angle}\n')
            

            # calculate error
            shoulder_error  = abs(shoulder_angle_anchor - shoulder_pot)
            elbow_error = abs(elbow_angle_anchor - elbow_pot)
