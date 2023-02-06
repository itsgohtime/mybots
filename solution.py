import numpy 
import pyrosim.pyrosim as pyrosim
import random
import os
import time 
import constants as c

class SOLUTION:
    def __init__(self, ID):
        self.weights_1 =  numpy.random.rand(c.numSensorNeurons, c.numHiddenNeurons) * 2 - 1
        self.weights_2 =  numpy.random.rand(c.numHiddenNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = ID

    def Start_Simulation(self, directOrGUI):
        if self.myID == 0:
            self.Create_World()
            self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID)) 

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness"+ str(self.myID) + ".txt"
        while (not os.path.exists(fitnessFileName)):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness_x = float(f.read())
        f.close()
        os.system("del " + fitnessFileName)

    def Mutate(self):
        matrix = random.randint(0,1)
        if (matrix == 0):
            randomRow = random.randint(0,c.numSensorNeurons - 1)
            randomColumn = random.randint(0,c.numHiddenNeurons - 1)
            self.weights_1[randomRow,randomColumn] =  random.random() * 2 - 1
        else: 
            randomRow = random.randint(0,c.numHiddenNeurons - 1)
            randomColumn = random.randint(0,c.numMotorNeurons - 1)
            self.weights_2[randomRow,randomColumn] =  random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos = [3,3,3.2], size = [1,1,0.5])
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos = [0,0,1.8], size = [0.5, 0.8, 1])
        pyrosim.Send_Joint(name = "Torso_LThigh", parent= "Torso", child = "LThigh", type = "revolute", position = [0, -0.35, 1.3], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LThigh", pos = [0,0,-0.3], size = [0.3,0.3,0.6])
        pyrosim.Send_Joint(name = "LThigh_LShank", parent= "LThigh", child = "LShin", type = "revolute", position = [0, 0, -0.6], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LShank", pos = [0,0,-0.35], size = [0.3,0.3,0.7])
        pyrosim.Send_Joint(name = "Torso_RThigh", parent= "Torso", child = "RThigh", type = "revolute", position = [0, 0.35, 1.3], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RThigh", pos = [0,0,-0.3], size = [0.3,0.3,0.6])
        pyrosim.Send_Joint(name = "RThigh_RShank", parent= "RThigh", child = "RShin", type = "revolute", position = [0, 0, -0.6], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RShank", pos = [0,0,-0.35], size = [0.3,0.3,0.7])
        pyrosim.Send_Joint(name = "Torso_LArm", parent= "Torso", child = "LArm", type = "revolute", position = [0, -0.4, 2.15], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LArm", pos = [0,-0.15,-0.4], size = [0.3,0.3,0.8])
        pyrosim.Send_Joint(name = "Torso_RArm", parent= "Torso", child = "RArm", type = "revolute", position = [0, 0.4, 2.15], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RArm", pos = [0,0.15,-0.4], size = [0.3,0.3,0.8])
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "LShank")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "RShank")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LArm")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RArm")
        pyrosim.Send_Hidden_Neuron(name = 4)
        pyrosim.Send_Hidden_Neuron(name = 5)
        pyrosim.Send_Hidden_Neuron(name = 6)
        pyrosim.Send_Hidden_Neuron(name = 7)
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_LThigh")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_RThigh")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "LThigh_LShank")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "RThigh_RShank")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_LArm")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_RArm")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse(
                    currentRow , 
                    currentColumn + c.numSensorNeurons , 
                    self.weights_1[currentRow][currentColumn]) 
        for currentRow in range(c.numHiddenNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( 
                    c.numSensorNeurons + currentRow , 
                    currentColumn + c.numSensorNeurons + c.numHiddenNeurons, 
                    self.weights_2[currentRow][currentColumn]) 
        pyrosim.End()
