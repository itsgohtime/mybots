from simulation import SIMULATION   
import sys

directOrGUI = sys.argv[1] 
solutionID = sys.argv[2]
simulate = SIMULATION(directOrGUI, solutionID)
simulate.RUN()
simulate.Get_Fitness(solutionID)