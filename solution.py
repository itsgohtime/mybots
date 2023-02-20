import numpy 
import pyrosim.pyrosim as pyrosim
import random
import os
import time 
import constants as c

class SOLUTION:
    def __init__(self):
        self.name = 0
        self.directions = [0, 0, 0, 0, 0, 0]
        while sum(self.directions) < 3:
            self.directions = numpy.random.randint(2, size = 6)
        self.link_per = numpy.random.randint(2,4, size = 6)
        self.num_of_links = 1
        for i in range(6):
            if self.directions[i]:
                self.num_of_links += self.link_per[i]
        self.sensors = numpy.random.randint(2, size=self.num_of_links)

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
        self.w, self.l, self.h = self.Link_Size(0)
        self.Create_Link(0, 0, 2, self.w, self.l, self.h)
        self.name += 1
        for i in range(6):
            if self.directions[i]:
                self.Generate_Arm(i)
                pass
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
        for i in range(6):
            if self.directions[i]:
                pyrosim.Send_Motor_Neuron( name = count , jointName = f"{0}_{name}")
                name += 1; count += 1
                for i in range(1,self.link_per[i]):
                    pyrosim.Send_Motor_Neuron(name = count , jointName = f"{name-1}_{name}")
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

    def Create_Link(self, x,  y, z,  width, length, height):
        match self.sensors[self.name]:
            case 0:
                pyrosim.Send_Cube(name=f"{self.name}", pos = [x, y, z], size = [width, length, height])
            case 1:
                 pyrosim.Send_Cube(name=f"{self.name}", pos = [x, y, z], size = [width, length, height], color = "green")

    def Create_Joint(self, x, y, z, parent, child):
        joint = random.randint(0,2)
        match joint:
            case 0:
                pyrosim.Send_Joint(name = f"{parent}_{child}", parent = f"{parent}", child = f"{child}", 
                               type = "revolute", position = [x, y, z], jointAxis = "0 0 1")
            case 1:
                pyrosim.Send_Joint(name = f"{parent}_{child}", parent = f"{parent}", child = f"{child}", 
                               type = "revolute", position = [x, y, z], jointAxis = "1 0 0")
            case 2:
                pyrosim.Send_Joint(name = f"{parent}_{child}", parent = f"{parent}", child = f"{child}", 
                               type = "revolute", position = [x, y, z], jointAxis = "0 1 0")
    
    def Generate_Arm(self, i):
        x = 0; y = 0; z = 2
        match i:
            case 0:
                x = self.w/2
                self.Create_Joint(x,y,z, 0, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(w/2, 0, 0, w, l, h)
                self.name += 1
                self.Create_Joint(w,0, 0, self.name - 1, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(w/2, 0, 0, w, l, h)
                self.name += 1
                prev_dir = 1
            case 1:
                x = -self.w/2
                self.Create_Joint(x,y,z, 0, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(-w/2, 0, 0, w, l, h)
                self.name += 1
                self.Create_Joint(-w,0, 0, self.name - 1, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(-w/2, 0, 0, w, l, h)
                self.name += 1
                prev_dir = 0
            case 2:
                y = self.l/2
                self.Create_Joint(x,y,z, 0, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(0, l/2, 0, w, l, h)
                self.name += 1
                self.Create_Joint(0,l, 0, self.name - 1, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(0, l/2, 0, w, l, h)
                self.name += 1
                prev_dir = 3
            case 3:
                y = -self.l/2
                self.Create_Joint(x,y,z, 0, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(0, -l/2, 0, w, l, h)
                self.name += 1
                self.Create_Joint(0,-l, 0,self.name - 1, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(0, -l/2, 0, w, l, h)
                self.name += 1
                prev_dir = 2
            case 4:
                z = z + self.h/2
                self.Create_Joint(x,y,z, 0, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(0, 0, h/2, w, l, h)
                self.name += 1
                self.Create_Joint(0,0, h,self.name - 1, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(0, 0, h/2, w, l, h)
                self.name += 1
                prev_dir = 5
            case 5:
                z = z-self.h/2
                self.Create_Joint(x,y,z, 0, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(0, 0, -h/2, w, l, h)
                self.name += 1
                self.Create_Joint(0,0, -h, self.name - 1, self.name)
                w,l,h = self.Link_Size(1)
                self.Create_Link(0, 0, -h/2, w, l, h)
                self.name += 1
                prev_dir = 4
        
        for j in range(2, self.link_per[i]):
            dir = random.randint(0,5)
            while dir == prev_dir:
                dir = random.randint(0,5)
            match dir:
                case 0:
                    x,y,z = self.Calculate_Joint(dir, prev_dir, w, l, h)
                    self.Create_Joint(x,y,z, self.name - 1, self.name)
                    w,l,h = self.Link_Size(j)
                    self.Create_Link(w/2, 0, 0, w, l, h)
                    self.name += 1
                    prev_dir = 1
                case 1:
                    x,y,z = self.Calculate_Joint(dir, prev_dir, w, l, h)
                    self.Create_Joint(x,y,z, self.name - 1, self.name)
                    w,l,h = self.Link_Size(j)
                    self.Create_Link(-w/2, 0, 0, w, l, h)
                    self.name += 1
                    prev_dir = 0
                case 2:
                    x,y,z = self.Calculate_Joint(dir, prev_dir, w, l, h)
                    self.Create_Joint(x,y,z, self.name - 1, self.name)
                    w,l,h = self.Link_Size(j)
                    self.Create_Link(0, l/2, 0, w, l, h)
                    self.name += 1
                    prev_dir = 3
                case 3:
                    x,y,z = self.Calculate_Joint(dir, prev_dir, w, l, h)
                    self.Create_Joint(x,y,z, self.name - 1, self.name)
                    w,l,h = self.Link_Size(j)
                    self.Create_Link(0, -l/2, 0, w, l, h)
                    self.name += 1
                    prev_dir = 2
                case 4:
                    x,y,z = self.Calculate_Joint(dir, prev_dir, w, l, h)
                    self.Create_Joint(x,y,z, self.name - 1, self.name)
                    w,l,h = self.Link_Size(j)
                    self.Create_Link(0, 0, h/2, w, l, h)
                    self.name += 1
                    prev_dir = 5
                case 5:
                    x,y,z = self.Calculate_Joint(dir, prev_dir, w, l, h)
                    self.Create_Joint(x,y,z, self.name - 1, self.name)
                    w,l,h = self.Link_Size(j)
                    self.Create_Link(0, 0, -h/2, w, l, h)
                    self.name += 1
                    prev_dir = 4
            
    def Link_Size(self, i):
        width = random.random()*(0.3 - i*0.08) + (0.3 - i*0.08)
        length = random.random()*(0.3 - i * 0.08) + (0.3 - i*0.08)
        height = random.random()*(0.3 - i*0.08) + (0.3 - i*0.08)
        return width, length, height

    def Calculate_Joint(self, dir, prev_dir, w, l, h):
        match prev_dir:
            case 0:
                match dir:
                    case 1:
                        x = -w; y = 0; z = 0
                    case 2:
                        x = -w/2;y = l/2; z = 0
                    case 3:
                        x = -w/2; y = -l/2; z = 0
                    case 4:
                        x = -w/2; y = 0; z = h/2
                    case 5:
                        x = -w/2; y = 0; z = -h/2
            case 1:
                match dir:
                    case 0:
                        x = w; y = 0; z = 0
                    case 2:
                        x = w/2;y = l/2; z = 0
                    case 3:
                        x = w/2; y = -l/2; z = 0
                    case 4:
                        x = w/2; y = 0; z = h/2
                    case 5:
                        x = w/2; y = 0; z = -h/2
            case 2:
                match dir:
                    case 0:
                        x = w/2; y = -l/2; z = 0
                    case 1:
                        x = -w/2; y = -l/2; z = 0
                    case 3:
                        x = 0; y = -l; z = 0
                    case 4:
                        x = 0; y = -l/2; z = h/2
                    case 5:
                        x = 0; y = -l/2; z = -h/2
            case 3:
                match dir:
                    case 0:
                        x = w/2; y = l/2; z = 0
                    case 1:
                        x = -w/2; y = l/2; z = 0
                    case 2:
                        x = 0; y = l; z = 0
                    case 4:
                        x = 0; y = l/2; z = h/2
                    case 5:
                        x = 0; y = l/2; z = -h/2
            case 4:
                match dir:
                    case 0:
                        x = w/2; y = 0; z = -h/2
                    case 1:
                        x = -w/2; y = 0; z = -h/2
                    case 2:
                        x = 0; y = l/2; z = -h/2
                    case 3:
                        x = 0; y = -l/2; z = -h/2
                    case 5:
                        x = 0; y = 0; z = -h
            case 5:
                match dir:
                    case 0:
                        x = w/2; y = 0; z = h/2
                    case 1:
                        x = -w/2; y = 0; z = h/2
                    case 2:
                        x = 0; y = l/2; z = h/2
                    case 3:
                        x = 0; y = -l/2; z = h/2
                    case 4:
                        x = 0; y = 0; z = h
        return x, y, z
