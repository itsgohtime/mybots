import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box_towers.sdf")
length = 1; width = 1; height = 1
x = 0; y = 0; z = 0.5
for row in range(5):
    for col in range(5):
        for i in range(10):
            box_name = "Box" + str(x)
            pyrosim.Send_Cube(name=box_name, pos = [x, y, z + i], size = [length, width, height])
            length = 0.9 * length
            width = 0.9 * width
            height = 0.9 * height
        length = 1; width = 1; height = 1
        x += 1
    x = 0
    y += 1
pyrosim.End()