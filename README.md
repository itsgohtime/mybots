# Asn 5 Documentation

### How to run 
1. Open start.py and run the file to run Asn_7

### About the codebase
- start.py, simulate.py, simulation.py have the code to run the simulation
- motor.py, sensor.py, robot.py have the code to create the parts of the robot
- solution.py has the code to create the body and brain of the robot
- world.py has the code to create the world of the simulation
- constants.py has the constants used in the codebase

### What I Did?
-  Created a program that generates a creature that branches into 3D with a:
    - random number (3-6) of arms of 
    - random number (2-4) of
    - randomly shaped links (see "How bodies are formed") with
    - random sensor placement
        - Links with and without sensors are colored green and blue, respectively.

### How bodies are formed
- First 2 links are in the direction that the arm protrudes
    - if arm protrudes in +x, then the first 2 links attach in the +x direction
- Any extra links attach in a random direction that is not where the previous link is
    - Relative joint positions are found using the direction of new link and direction of previous link
- The main link of the body is from 0.5 to 0.75, the next 2 links are from 0.22 to 0.46, the third link is from 0.14 to 0.3, and the fourth link is from 0.06 to 0.14
    - The decreasing size with each link makes it so that if an arm were to curl back on itself it would not be able to intersect with other arms
![alt text](https://github.com/itsgohtime/mybots/blob/Asn-7/body_diagram.jpg)

### How brains are fomred
-
![Alt text](relative/path/to/brain_diagam.jpg?raw=true "Diagram of Body")

### Citations 
- This work was built on top of ludobots and pyrosim
    - https://www.reddit.com/r/ludobots/wiki/finalproject/
    - https://github.com/jbongard/pyrosim 
