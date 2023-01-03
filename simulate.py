import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import time
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
pyrosim.Prepare_To_Simulate(robotID)

amplitude_bl = 0
frequency_bl = 10
phaseOffset_bl = 0
amplitude_fl = -numpy.pi/4
frequency_fl = 10
phaseOffset_fl = 0
x = numpy.linspace(0, 2*numpy.pi, 1000) 
targetangles_bl = amplitude_bl * numpy.sin(frequency_bl * x + phaseOffset_bl)
targetangles_fl = amplitude_fl * numpy.sin(frequency_fl * x + phaseOffset_fl)
#numpy.save("data/targetangles_bl", targetangles_bl)
#numpy.save("data/targetangles_fl", targetangles_fl)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(robotID, b'Torso_BackLeg', p.POSITION_CONTROL, targetangles_bl[i], 25)
    pyrosim.Set_Motor_For_Joint(robotID, b'Torso_FrontLeg', p.POSITION_CONTROL, targetangles_fl[i], 25)
    time.sleep(1/240)
numpy.save("data/backLegSensorValues", backLegSensorValues)
numpy.save("data/frontLegSensorValues", frontLegSensorValues)
p.disconnect()