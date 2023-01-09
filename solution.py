import numpy 
import pyrosim.pyrosim as pyrosim
import random
import os
import time 

class SOLUTION:
    def __init__(self, ID):
        self.weights =  numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.myID = ID

    def Start_Simulation(self, directOrGUI):
        if self.myID == 0:
            self.Create_World()
            self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID) + " 2>&1") 

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness"+ str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del " + fitnessFileName)

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow,randomColumn] =  random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos = [-3,3,0.5], size = [1,1,1])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos = [1.5,0,1.5], size = [1,1,1])
        pyrosim.Send_Joint(name = "Torso_FrontLeg", parent= "Torso", child = "FrontLeg", type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos = [0.5,0,-0.5], size = [1,1,1])
        pyrosim.Send_Joint(name = "Torso_BackLeg", parent= "Torso", child = "BackLeg", type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos = [-0.5,0,-0.5], size = [1,1,1])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( currentRow , currentColumn + 3 , self.weights[currentRow][currentColumn]) 
        pyrosim.End()
