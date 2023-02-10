import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time 
import numpy
import os

from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT()
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        pyrosim.Prepare_To_Simulate(self.robot.robotID)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
        self.heights = numpy.zeros(1000)
        self.box_heights = numpy.zeros(1000)

    def RUN(self):
        for i in range(1000):
            p.stepSimulation()
            self.robot.SENSE(i)
            self.robot.THINK()
            self.robot.ACT(i)
            if self.directOrGUI == "GUI":
                time.sleep(1/1000)

    def __del__(self):
        p.disconnect()

    