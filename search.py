import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import time

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()