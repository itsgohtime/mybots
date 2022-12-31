import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeID = p.loadURDF("plane.urdf")
robotID = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
backLegSensorValues = numpy.zeros(1000)
pyrosim.Prepare_To_Simulate(robotID)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    time.sleep(1/60)
print(backLegSensorValues)
p.disconnect()
