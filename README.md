# Asn 8 Documentation

### How to run 
1. Open constants.py to change number of generations and population size
2. Open search.py and run the file to run Asn_8 for seeds 0, 1, 2, 3, and 4
    - The seeds can be also changed in search.py by changing what the for loop variable num is 
        - For example, change line 9 to "for num in [1, 2, 3, 4, 5]" to have seeds 1, 2, 3, 4, and 5
3. When each simulation is finished, it will prompt if you are ready; any input will cause the final simulation and plot to be shown.
4. The next seed will run when the plot is closed. 

### Citations 
- This work was built on top of ludobots and pyrosim
    - https://www.reddit.com/r/ludobots/wiki/finalproject/
    - https://github.com/jbongard/pyrosim 

### What I Did?
- Created a program that generates a creature that branches into 3D with a:
    - random shaped number (5-8) links with
    - random sensor placement
        - Links with and without sensors are colored green and blue, respectively
    - that can mutate to maximize distance traveled using parallel hill climber
        - fitness = distance_traveled
        - evolved for 200 generations with a population size of 25
        ![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/fitness_curves.jpeg)

### Bodies
- How bodies are formed
    - Based on the number of links, a direction for each joint is randomly chosen
    - The first direction connects the second link to the first link and then links are added like a binary tree
        - third and fourth link join to second link
        - fifth and sixth link join to third link
        - seventh and eight link join to fourth link
    - The sizes of the links are checked to ensure they don't collid with previous links
        - If there is a collision, the dimensions are chosen again and this continues until there isn't a collision
![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/body_diagram.jpg)
- How bodies are mutated
    - A random link excluding the first one is chosen and the direction it attaches to the previous link is changed
    - Following links's direction are also changed to ensure that there is no overlap and if there is any links that would collide with a previous link then the dimensions are changed
![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/mutated_body.jpg)

### Brains
- How brains are formed
    - The number of links that are sensors are stored and each is made to be a sensor neuron
    - There are 4 hidden neurons but it can be changed in constants.py
    - Each joint (number of links - 1) is made to be a motor neuron
    - Each sensor neuron is connected to every hidden neuron and every hidden neuron is connected to every motor neuron
    ![alt text](https://github.com/itsgohtime/mybots/blob/Asn-8/brain_diagram.jpg)
- How brains are mutated
    - A random synapse (arrow in the diagram above) either connecting a sensor neuron to a hidden neuron or a motor neuron is chosen and then the weight is changed within the range of [-1, 1]

### About the codebase
- search.py, simulate.py, simulation.py have the code to run the simulation
- motor.py, sensor.py, robot.py have the code to create the parts of the robot
- parallelHillClimber.py has the code to evolve the robot
- solution.py has the code to create the body and brain of the robot as well as mutates it
- world.py has the code to create the world of the simulation
- constants.py has the constants used in the codebase