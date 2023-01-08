import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self): #how to put in specific variables
        self.amplitude = -numpy.pi/4
        if self.jointName == b'Torso_FrontLeg':
            self.frequency = 10
        else:
            self.frequency = 5
        self.offset = 0
        x = numpy.linspace(0, 2*numpy.pi, 1000) 
        self.motorValues = self.amplitude * numpy.sin(self.frequency * x + self.offset)

    def Set_Value(self, t, robot):
        pyrosim.Set_Motor_For_Joint(robot, self.jointName, p.POSITION_CONTROL,self.motorValues[t], 25)

    def Save_values(self):
        fileName = "data/targetangles_" + self.jointName 
        numpy.save(fileName, self.motorValues)