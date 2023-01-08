import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, desiredAngle, robot):
        pyrosim.Set_Motor_For_Joint(robot, self.jointName, p.POSITION_CONTROL, desiredAngle, 25)
