import pybullet as p
import pybullet_data

class WORLD:
    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.planeID = p.loadURDF("plane.urdf")
        self.objects = p.loadSDF("world.sdf")
