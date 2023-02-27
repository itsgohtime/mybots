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
-  I did stuff

### Bodies
- How bodies are formed
    - we did this
![alt text](https://github.com/itsgohtime/mybots/blob/Asn-7/body_diagram.jpg)
- How bodies are mutated

### Brains
- How brains are formed
    - The number of links that are sensors are stored and each is made to be a sensor neuron
    - There are 4 hidden neurons but it can be changed in constants.py
    - Each joint (number of links - 1) is made to be a motor neuron
    - Each sensor neuron is connected to every hidden neuron and every hidden neuron is ocnnected to every motor neuron
    ![alt text](https://github.com/itsgohtime/mybots/blob/Asn-7/brain_diagram.jpg)
- How brains are mutated

### About the codebase
- search.py, simulate.py, simulation.py have the code to run the simulation
- motor.py, sensor.py, robot.py have the code to create the parts of the robot
- parallelHillClimber.py has the code to evolve the robot
- solution.py has the code to create the body and brain of the robot as well as mutates it
- world.py has the code to create the world of the simulation
- constants.py has the constants used in the codebase