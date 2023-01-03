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
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(robotID, b'Torso_BackLeg', p.POSITION_CONTROL, (3.14*random.random()) - (3.14/2), 25)
    pyrosim.Set_Motor_For_Joint(robotID, b'Torso_FrontLeg', p.POSITION_CONTROL, (3.14*random.random()) - (3.14/2), 25)
    time.sleep(1/60)
numpy.save("data/backLegSensorValues", backLegSensorValues)
numpy.save("data/frontLegSensorValues", frontLegSensorValues)
p.disconnect()
