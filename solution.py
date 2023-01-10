import numpy 
import pyrosim.pyrosim as pyrosim
import random
import os
import time 
import constants as c

class SOLUTION:
    def __init__(self, ID):
        self.weights =  numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights = self.weights * 2 - 1
        self.myID = ID

    def Start_Simulation(self, directOrGUI):
        if self.myID == 0:
            self.Create_World()
            self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID)) 

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness"+ str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del " + fitnessFileName)

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons - 1)
        randomColumn = random.randint(0,c.numMotorNeurons - 1)
        self.weights[randomRow,randomColumn] =  random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos = [-3,3,0.5], size = [1,1,1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos = [0,0,1], size = [1,1,1])
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos = [0,0.5,0], size = [0.2,1,0.2])
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [0,-0.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos = [0,-0.5,0], size = [0.2,1,0.2])
        pyrosim.Send_Joint(name = "Torso_LeftLeg", parent= "Torso", child = "LeftLeg", type = "revolute", position = [-0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos = [-0.5,0,0], size = [1,0.2,0.2])
        pyrosim.Send_Joint(name = "Torso_RightLeg", parent= "Torso", child = "RightLeg", type = "revolute", position = [0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos = [0.5,0,0], size = [1,0.2,0.2])
        pyrosim.Send_Joint(name = "FrontLeg_FLowerLeg", parent= "FrontLeg", child = "FLowerLeg", type = "revolute", position = [0, 1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FLowerLeg", pos = [0,0,-0.5], size = [0.2,0.2,1])
        pyrosim.Send_Joint(name = "BackLeg_BLowerLeg", parent= "BackLeg", child = "BLowerLeg", type = "revolute", position = [0, -1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BLowerLeg", pos = [0,0,-0.5], size = [0.2,0.2,1])
        pyrosim.Send_Joint(name = "LeftLeg_LLowerLeg", parent= "LeftLeg", child = "LLowerLeg", type = "revolute", position = [-1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LLowerLeg", pos = [0,0,-0.5], size = [0.2,0.2,1])
        pyrosim.Send_Joint(name = "RightLeg_RLowerLeg", parent= "RightLeg", child = "RLowerLeg", type = "revolute", position = [1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RLowerLeg", pos = [0,0,-0.5], size = [0.2,0.2,1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontLeg_FLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeg_BLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LeftLeg_LLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RightLeg_RLowerLeg")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( currentRow , currentColumn + c.numSensorNeurons , self.weights[currentRow][currentColumn]) 
        pyrosim.End()
