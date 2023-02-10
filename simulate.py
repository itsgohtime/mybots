from simulation import SIMULATION   
import sys

directOrGUI = sys.argv[1] 
simulate = SIMULATION(directOrGUI)
simulate.RUN()
