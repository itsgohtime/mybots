pass

# import pybullet as p
# import pyrosim.pyrosim as pyrosim
# import pybullet_data
# import constants as c
# import numpy
# import time
# import random

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.setGravity(0,0,-9.8)
# planeID = p.loadURDF("plane.urdf")
# robotID = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotID)

# x = numpy.linspace(0, 2*numpy.pi, 1000) 
# targetangles_bl = c.amplitude_bl * numpy.sin(c.frequency_bl * x + c.phaseOffset_bl)
# targetangles_fl = c.amplitude_fl * numpy.sin(c.frequency_fl * x + c.phaseOffset_fl)
# #numpy.save("data/targetangles_bl", targetangles_bl)
# #numpy.save("data/targetangles_fl", targetangles_fl)  
# print(c.backLegSensorValues)
# for i in range(1000):
#     p.stepSimulation()
#     c.backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     c.frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(robotID, b'Torso_BackLeg', p.POSITION_CONTROL, targetangles_bl[i], 25)
#     pyrosim.Set_Motor_For_Joint(robotID, b'Torso_FrontLeg', p.POSITION_CONTROL, targetangles_fl[i], 25)
#     time.sleep(1/240)
# #numpy.save("data/backLegSensorValues", c.backLegSensorValues)
# #numpy.save("data/frontLegSensorValues", c.frontLegSensorValues)
# p.disconnect()