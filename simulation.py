import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time 
import numpy

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT()
        p.setAdditionalSearchPath(pybullet_data.getDataPath()) #why is this here and not in world
        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(self.robot.robotID)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def RUN(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.SENSE(i)
            self.robot.THINK()
            self.robot.ACT(i)
            time.sleep(1/120)

    def __del__(self):
        p.disconnect()
        
        