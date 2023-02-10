import numpy 
import pyrosim.pyrosim as pyrosim
import random
import os
import time 
import constants as c

class SOLUTION:
    def __init__(self):
        self.name = 0
        self.links = random.randint(3,8)
        self.sensors = numpy.random.randint(2, size=self.links)
        print(self.sensors)

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python3 simulate.py " + directOrGUI) 

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        width = random.random()*0.75 + 0.25; length = random.random()*0.75 + 0.25; height = random.random()*0.75 + 0.25
        self.cube(0, height/2 + 0.2, width, length, height)
        self.name += 1
        pyrosim.Send_Joint(name = f"{self.name-1}_{self.name}", parent = f"{self.name-1}", child = f"{self.name}", 
                           type = "revolute", position = [0, length/2, height/2 + 0.2], jointAxis = "0 0 1")
        width = random.random()*0.75 + 0.25; length = random.random()*0.75 + 0.625; height = random.random()*0.75 + 0.25
        self.cube(length/2, 0, width, length, height)
        self.name += 1
        for i in range(self.links - 2):
            pyrosim.Send_Joint(name = f"{self.name-1}_{self.name}", parent = f"{self.name-1}", child = f"{self.name}", 
                               type = "revolute", position = [0, length, 0], jointAxis = "0 0 1")
            width = random.random()*0.75 + 0.25; length = random.random()*0.75 + 0.25; height = random.random()*0.75 + 0.25
            self.cube(length/2, 0, width, length, height)
            self.name += 1
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        count = 0
        for i in range(self.name):
            if (self.sensors[i]):
                pyrosim.Send_Sensor_Neuron(name = count , linkName = f"{i}")
                count += 1
        numSensorNeurons = count
        for i in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name = count)
            count += 1
        name = 1
        for i in range(self.name - 1):
            pyrosim.Send_Motor_Neuron( name = count , jointName = f"{name-1}_{name}")
            name += 1; count += 1
        self.weights_1 =  numpy.random.rand(numSensorNeurons, c.numHiddenNeurons) * 2 - 1
        self.weights_2 =  numpy.random.rand(c.numHiddenNeurons, self.name - 1) * 2 - 1
        for currentRow in range(numSensorNeurons):
            for currentColumn in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse(
                    currentRow , 
                    currentColumn + numSensorNeurons , 
                    self.weights_1[currentRow][currentColumn]) 
        for currentRow in range(c.numHiddenNeurons):
            for currentColumn in range(self.name - 1):
                pyrosim.Send_Synapse( 
                    numSensorNeurons + currentRow , 
                    currentColumn + numSensorNeurons + c.numHiddenNeurons, 
                    self.weights_2[currentRow][currentColumn]) 
        pyrosim.End()

    def cube(self, y, z,  width, length, height):
        match self.sensors[self.name]:
            case 0:
                pyrosim.Send_Cube(name=f"{self.name}", pos = [0, y, z], size = [width, length, height])
            case 1:
                 pyrosim.Send_Cube(name=f"{self.name}", pos = [0, y, z], size = [width, length, height], color = "green")
