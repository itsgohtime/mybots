import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
import time
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.robotID = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + solutionID + ".nndf")
        os.system("del brain" + str(solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def SENSE(self, t):
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def ACT(self, t): 
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = bytes(self.nn.Get_Motor_Neurons_Joint(neuronName), 'utf-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle, self.robotID) 

    def THINK(self):
        self.nn.Update()

    def Get_Fitness(self,solutionID):
        xPosition = p.getBasePositionAndOrientation(self.robotID)[0][0]
        f = open("tmp" + solutionID + ".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.system("rename tmp" + solutionID + ".txt fitness" + solutionID + ".txt")

        

