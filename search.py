import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import time
import matplotlib.pyplot as plt
import constants as c
import numpy

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
best_fitness = numpy.zeros(c.numberOfGenerations)
for i in range(c.numberOfGenerations):
    best_fitness[i] = max(phc.fitness[i])
gen = list(range(c.numberOfGenerations))
plt.plot(gen, best_fitness)
plt.show()