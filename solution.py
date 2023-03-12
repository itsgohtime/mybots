import numpy 
import pyrosim.pyrosim as pyrosim
import random       
import os
import time 
import math
import constants as c

class SOLUTION:
    def __init__(self, ID):
        self.myID = ID
        self.name = 0
        self.num_of_links = random.randint(5, 8)
        self.Get_Directions()
        self.link_dim = numpy.zeros((self.num_of_links, 3))
        self.Get_Space()
        self.Ground()
        self.sensors = numpy.random.randint(2, size=self.num_of_links)
        self.joints = numpy.random.randint(3, size = self.num_of_links - 1)
        self.numSensorNeurons = sum(self.sensors)
        while (self.numSensorNeurons == 0):
            self.sensors = numpy.random.randint(2, size=self.num_of_links)
            self.numSensorNeurons = sum(self.sensors)
        self.numMotorNeurons = self.num_of_links-1
        self.weights_1 =  numpy.random.rand(self.numSensorNeurons, c.numHiddenNeurons) * 2 - 1
        self.weights_2 =  numpy.random.rand(c.numHiddenNeurons, self.numMotorNeurons) * 2 - 1
    
    def Start_Simulation(self, directOrGUI, seed):
        self.name = 0
        if self.myID == 0:
            self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        #if directOrGUI == "GUI":
        #    os.system("copy body" + str(self.myID) + ".urdf best_robots")
        #    os.rename(f"best_robots/body{self.myID}.urdf", f"best_robots/body{seed}.urdf")
        #    os.system("copy brain" + str(self.myID) + ".nndf best_robots")
        #    os.rename(f"best_robots/brain{self.myID}.nndf", f"best_robots/brain{seed}.nndf")
        os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID)) 

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness"+ str(self.myID) + ".txt"
        while True:
            try:
                f = open(fitnessFileName, "r")
                break
            except:
                pass
        self.fitness = float(f.read())
        f.close()
        os.system("del " + fitnessFileName)

    def Mutate(self):
        joint = random.randint(0, self.num_of_links-1)
        for i in range(joint, self.num_of_links-1):
            if i == 0:
                self.dir[0] = random.randint(0,5); self.prev_dir[0] = prev_dir(self.dir[0])
            else:
                self.dir[i] = random.randint(0,5)
                parent = int((i-1)/2)
                if 2*parent+2 == len(self.dir):
                    while (self.prev_dir[parent] == self.dir[i]):
                        self.dir[i] = random.randint(0,5)
                else:
                    while (self.prev_dir[parent] == self.dir[i] or self.dir[2*parent+1] == self.dir[2*parent+2]):
                        self.dir[i] = random.randint(0,5)
                self.prev_dir[i] = prev_dir(self.dir[i])
        self.Get_Space()
        self.Ground()
        matrix = random.randint(0,1)
        if (matrix == 0):
            randomRow = random.randint(0,self.numSensorNeurons - 1)
            randomColumn = random.randint(0,c.numHiddenNeurons - 1)
            self.weights_1[randomRow,randomColumn] =  random.random() * 2 - 1
        else: 
            randomRow = random.randint(0,c.numHiddenNeurons - 1)
            randomColumn = random.randint(0,self.numMotorNeurons - 1)
            self.weights_2[randomRow,randomColumn] =  random.random() * 2 - 1

    def Set_ID(self, ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        x = 0; y = 0; z = self.start_z
        w,l,h = self.link_dim[0]
        self.Create_Link(x, y, z,  w, l, h)
        self.name += 1
        match self.dir[0]:
                case 0:
                    self.Create_Joint(x+w/2, y, z, self.name - 1, self.name)
                case 1:
                    self.Create_Joint(x-w/2, y, z, self.name - 1, self.name)
                case 2:
                    self.Create_Joint(x, y+l/2, z, self.name - 1, self.name)
                case 3:
                    self.Create_Joint(x, y-l/2, z, self.name - 1, self.name)
                case 4:
                    self.Create_Joint(x, y, z+h/2, self.name - 1, self.name)
                case 5:
                    self.Create_Joint(x, y, z-h/2, self.name - 1, self.name)
        for i in range(1, self.num_of_links-1):
            w,l,h = self.link_dim[i]
            match self.dir[i-1]:
                case 0:
                    self.Create_Link(w/2, 0, 0,  w, l, h)
                case 1:
                    self.Create_Link(-w/2, 0, 0,  w, l, h)
                case 2:
                    self.Create_Link(0, l/2, 0,  w, l, h)
                case 3:
                    self.Create_Link(0, -l/2, 0,  w, l, h)
                case 4:
                    self.Create_Link(0, 0, h/2,  w, l, h)
                case 5:
                    self.Create_Link(0, 0, -h/2,  w, l, h)
            self.name += 1
            parent = math.floor((self.name -2)/2) + 1
            w,l,h = self.link_dim[parent]
            x,y,z = self.Calculate_Joint(self.dir[i], self.prev_dir[int((i-1)/2)], w, l, h)
            self.Create_Joint(x, y, z, parent, self.name)
        w,l,h = self.link_dim[-1]
        match self.dir[-1]:
            case 0:
                self.Create_Link(w/2, 0, 0,  w, l, h)
            case 1:
                self.Create_Link(-w/2, 0, 0,  w, l, h)
            case 2:
                self.Create_Link(0, l/2, 0,  w, l, h)
            case 3:
                self.Create_Link(0, -l/2, 0,  w, l, h)
            case 4:
                self.Create_Link(0, 0, h/2,  w, l, h)
            case 5:
                self.Create_Link(0, 0, -h/2,  w, l, h)
        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        count = 0
        for i in range(self.name):
            if (self.sensors[i]):
                pyrosim.Send_Sensor_Neuron(name = count , linkName = f"{i}")
                count += 1
        numSensorNeurons = count
        for i in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name = count)
            count += 1
        link_name = 0
        for i in range(1, self.num_of_links):
            if i == 1:
                pyrosim.Send_Motor_Neuron( name = count , jointName = "0_1")
                count += 1
            else:
                parent = math.floor((i -2)/2) + 1
                pyrosim.Send_Motor_Neuron( name = count , jointName = f"{parent}_{i}")
                count += 1
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
        joint = self.joints[child-1]
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
            
    def Link_Size(self, i):
        if i == 0:
            m = 0
        elif i == 1:
            m = 0
        elif i == 2 or i == 3:
            m = 1
        else:
            m = 2

        width = random.random()*(0.5 - (m * 0.1)) + 0.5 - (m * 0.1)
        length = random.random()*(0.5 - (m * 0.1)) + 0.5 - (m * 0.1)
        height = random.random()*(0.5 - (m * 0.1)) + 0.5 - (m * 0.1)
        return [width, length, height]

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
    
    def Check_Link(self, i):
        min_x, max_x, min_y, max_y, min_z, max_z = self.space[i]
        for j in range(i):
            cmin_x, cmax_x, cmin_y, cmax_y, cmin_z, cmax_z = self.space[j]
            if min_x < cmax_x and min_x > cmin_x and (min_y < cmax_y and max_y > cmin_y) and (min_z < cmax_z and max_z > cmin_z):
                return True
            elif max_x > cmin_x and max_x < cmax_x and (min_y < cmax_y and max_y > cmin_y) and (min_z < cmax_z and max_z > cmin_z):
                return True
            elif min_y < cmax_y and min_y > cmin_y and (min_x < cmax_x and max_x > cmin_x) and (min_z < cmax_z and max_z > cmin_z):
                return True
            elif max_y > cmin_y and max_y < cmax_y and (min_x < cmax_x and max_x > cmin_x) and (min_z < cmax_z and max_z > cmin_z):
                return True
            elif min_z < cmax_z and min_z > cmin_z and (min_x < cmax_x and max_x > cmin_x) and (min_y < cmax_y and max_y > cmin_y):
                return True
            elif max_z > cmin_z and max_z < cmax_z and (min_x < cmax_x and max_x > cmin_x) and (min_y < cmax_y and max_y > cmin_y):
                return True
        return False
    
    def find_space(self, i):
        if i == 1:
            parent = 0
        else:
            parent = math.floor((i -2)/2) + 1
        min_x, max_x, min_y, max_y, min_z, max_z = self.space[parent]
        w, l, h = self.link_dim[i]
        x = (min_x + max_x)/2
        y = (min_y + max_y)/2
        z = (min_z + max_z)/2
        match self.dir[i-1]:
            case 0:
                self.space[i] = [max_x, max_x + w, y - l/2, y + l/2, z - h/2, z + h/2]
            case 1:
                self.space[i] = [min_x - w, min_x, y - l/2, y + l/2, z - h/2, z + h/2]
            case 2:
                self.space[i] = [x - w/2, x + w/2, max_y, max_y + l, z - h/2, z + h/2]
            case 3:
                self.space[i] = [x - w/2, x + w/2, min_y - l, min_y, z - h/2, z + h/2]
            case 4:
                self.space[i] = [x - w/2, x + w/2, y - l/2, y + l/2, max_z, max_z + h]
            case 5:
                self.space[i] = [x - w/2, x + w/2, y - l/2, y + l/2, min_z - h, min_z]

    def Ground(self):
        min_z = min(self.space[:,4])
        for i in range(self.num_of_links):
            self.space[i,4] -= min_z
            self.space[i,5] -= min_z
        self.start_z = (self.space[0,5] - self.space[0,4])/2 + self.space[0,4]

    def Get_Directions(self):
        self.dir = numpy.zeros(self.num_of_links-1); self.prev_dir = numpy.zeros(self.num_of_links-1)
        self.dir[0] = random.randint(0,5); self.prev_dir[0] = prev_dir(self.dir[0])
        for i in range(1, self.num_of_links-1):
            self.dir[i] = random.randint(0,5)
            parent = int((i-1)/2)
            if 2*parent+2 == len(self.dir):
                while (self.prev_dir[parent] == self.dir[i]):
                    self.dir[i] = random.randint(0,5)
            else:
                while (self.prev_dir[parent] == self.dir[i] or self.dir[2*parent+1] == self.dir[2*parent+2]):
                    self.dir[i] = random.randint(0,5)
            self.prev_dir[i] = prev_dir(self.dir[i])

    def Get_Space(self):
        self.space = numpy.zeros((self.num_of_links, 6))
        x = 0; y = 0; z = 2
        self.link_dim[0] = self.Link_Size(0)
        w,l,h = self.link_dim[0]
        self.space[0] = [x-w/2, x+w/2, y-l/2, y+l/2, z-h/2, z+h/2]
        for i in range(1,self.num_of_links):
            self.link_dim[i] = self.Link_Size(i)
            w,l,h = self.link_dim[i]
            self.find_space(i)
            count = 0
            while (self.Check_Link(i)):
                self.link_dim[i] = self.Link_Size(i)
                w,l,h = self.link_dim[i]
                self.find_space(i)
                count += 1
                if count == 50:
                    self.link_dim[i] = [0, 0, 0]
                    w,l,h = self.link_dim[i]
                    self.find_space(i)

def prev_dir(dir):
    match dir:
        case 0:
            return 1
        case 1:
            return 0
        case 2:
            return 3
        case 3:
            return 2
        case 4:
            return 5
        case 5:
            return 4