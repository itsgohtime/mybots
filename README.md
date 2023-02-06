# Asn 5 Documentation

### How to run 
1. Open constants.py to change temperature and number of runs per temperature
2. Open search.py and run the file to run Asn 5
3. When simulation is finished, it will prompt if you are ready; any input will cause the final result to be shown. 

### What I Did?
- Built a biped based on ludobots final project documentation. Dimensions for links and positions of links and joints can be 
seen in following diagram.
    - Resource for ludobots final project: https://www.reddit.com/r/ludobots/wiki/finalproject/
- Neural network includes sensors at both arms and shanks with 4 hidden neurons to motor neurons for all 6 joints.
- Multi-objective function using a rank order centroid weights {fitness = dist_traveled + 2 * avg_height + 3 * final_height}
    - Fitness function prioritizes biped standing up straight for the majority of the simulation with an emphasize on the
    final height of the robot while also trying to maximize distance traveled.
    - Resource for multi-objective function: https://www.tandfonline.com/doi/full/10.1080/23311916.2018.1502242#:~:text=The%20dominance%20solution%20and%20optimal
- Replaced optimization method of PHC with simulated annealing using linear reduction rule for annealing schedule
    - Resource for simulated annealing: https://towardsdatascience.com/optimization-techniques-simulated-annealing-d6a4785a1de7

### Citations
- https://www.reddit.com/r/ludobots/wiki/finalproject/
- https://www.tandfonline.com/doi/full/10.1080/23311916.2018.1502242#:~:text=The%20dominance%20solution%20and%20optimal
- https://towardsdatascience.com/optimization-techniques-simulated-annealing-d6a4785a1de7
