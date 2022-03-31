import os
import sys

import arm_angle_collection_class as arm
# path might be wrong
obj_arm = arm.arm_angle_collection()

sys.path.append(os.path.realpath('../../../base_project'))

from brachiograph import BrachioGraph

class BrachioGraphError(BrachioGraph):

    def proportional_controller(set_point, process_variable):
         Kp = 0.8 #proportional gain
         error = set_point - process_variable
         output = Kp * error
         return output

    #Modified to use error correction
    def set_angles(self, angle_1 = None, angle_2=None):

        shoulder_angle_anchor = angle_1
        elbow_angle_anchor = angle_2

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


        # get pot values
        shoulder_pot, elbow_pot = obj_arm.angle_request()

        #get pot angles
        shoulder_pot, elbow_pot = #function(shoulder_pot,elbow_pot)

        # compare pots angles and servo angles
        set_angles_wrapped(angle_1, angle_2)

        # calculate error
        shoulder_error  = shoulder_angle_anchor - shoulder_pot
        elbow_error = elbow_angle_anchor - elbow_pot

        #set variables for P controller
        shoulder_angle = shoulder_angle_anchor
        elbow_angle = elbow_angle_anchor

        # determine if error is acceptable (for now, test with 1 degree error maximum)
        while (shoulder_error > 1 or elbow_error > 1):

                if (shoulder_error > 1):
                    shoulder_angle = shoulder_angle + proportional_controller(shoulder_angle_anchor,shoulder_pot)

                if (shoulder_error > 1):
                    elbow_angle = elbow_angle + proportional_controller(elbow_angle_anchor,elbow_pot)

                set_angles_wrapped(shoulder_angle, elbow_angle)

                # calculate error
                shoulder_error  = shoulder_angle_anchor - shoulder_pot
                elbow_error = elbow_angle_anchor - elbow_pot
