import os
import sys

sys.path.append(os.path.realpath('../../../base_project'))

from brachiograph import BrachioGraph

class BrachioGraphError(BrachioGraph):

    #Modify to use our code
    def xy(self, x=None, y=None, wait=0, interpolate=10, draw=False):
        """Moves the pen to the xy position; optionally draws while doing it."""

        wait = wait or self.wait

        if draw:
            self.pen.down()
        else:
            self.pen.up()

        x = x or self.x
        y = y or self.y

        (angle_1, angle_2) = self.xy_to_angles(x, y)

        # calculate how many steps we need for this move, and the x/y length of each
        (x_length, y_length) = (x - self.x, y - self.y)

        length = math.sqrt(x_length ** 2 + y_length **2)

        no_of_steps = int(length * interpolate) or 1

        if no_of_steps < 100:
            disable_tqdm = True
        else:
            disable_tqdm = False

        (length_of_step_x, length_of_step_y) = (x_length/no_of_steps, y_length/no_of_steps)

        for step in tqdm.tqdm(range(no_of_steps), desc='Interpolation', leave=False, disable=disable_tqdm):

            self.x = self.x + length_of_step_x
            self.y = self.y + length_of_step_y

            angle_1, angle_2 = self.xy_to_angles(self.x, self.y)

            self.set_angles(angle_1, angle_2)

            if step + 1 < no_of_steps:
                sleep(length * wait/no_of_steps)

        sleep(length * wait/10)
