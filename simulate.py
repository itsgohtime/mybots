import pybullet as p
import time

physicsClient = p.connect(p.GUI)
for x in range(1000):
    p.stepSimulation()
    time.sleep(1)
    print(x)
p.disconnect()