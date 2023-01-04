import pybullet as p
import numpy 

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

amplitude_bl = 0
frequency_bl = 10
phaseOffset_bl = 0
amplitude_fl = -numpy.pi/4
frequency_fl = 10
phaseOffset_fl = 0