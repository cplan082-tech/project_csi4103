import os
import sys

sys.path.append(os.path.realpath('../../../base_project'))

from BrachioGraphError import BrachioGraphError

bg = BrachioGraphError()

bg.park()

bg.plot_file("circle.json")
