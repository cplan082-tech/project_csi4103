import BrachioGraph

class BrachioGraphError(BrachioGraph):

    #Modify to use our code
    def set_angles(self, angle_1=None, angle_2=None):
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


        self.set_pulse_widths(pw_1, pw_2) # This moves the servos to the desired location

        """
        Error Correction Wrapper Code Here - Loop Function

        #get pot value

        #get pot2angle

        #calculate error

        #depending on error, either do nothing or recall function with new angles

        """


        self.x, self.y = self.angles_to_xy(self.angle_1, self.angle_2)
