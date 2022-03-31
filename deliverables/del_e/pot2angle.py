import math


# Init variables:
maxpotrange = 1023 # [(2**10)-1], Uncomment if connecting to 5V terminal on Arduino
#maxpotrange = 675 # [(2**10)*(3.3/5)-1], Uncomment if connecting to 3.3V terminal on Arduino
minangle = 0 # Set minimum angle of the potentiometers (if nessesary)
maxangle = 300 # Max angle of the potentiometers (B10kΩ has a turn angle of 300 degrees)
shoulder_modifier = 0 # Linear adjustment (set after calibration)
elbow_modifier = 0

#def pot2angle(potinput):
#	return potinput * (maxangle - minangle) / maxpotrange + modifier

def shoulder_motor_angle(shoulder_pot):
	return shoulder_pot * (maxangle - minangle) / maxpotrange + shoulder_modifier


def inner_angle(shoulder_pot):
	return shoulder_pot * (maxangle - minangle) / maxpotrange + shoulder_modifier


def hypotenuse_angle(shoulder_pot):
	return shoulder_pot * (maxangle - minangle) / maxpotrange + shoulder_modifier


def elbow_angle(elbow_pot):
	return elbow_pot * (maxangle - minangle) / maxpotrange + elbow_modifier


def elbow_motor_angle(elbow_pot):
	return 180 - (elbow_pot * (maxangle - minangle) / maxpotrange + elbow_modifier)
