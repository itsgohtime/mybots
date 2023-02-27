import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import time
import matplotlib.pyplot as plt
import constants as c
import numpy
import random

for num in [0, 1, 2, 3, 4]:
    random.seed(num)
    numpy.random.seed(num)
    phc = PARALLEL_HILL_CLIMBER()
    phc.Evolve()
    phc.Show_Best()
    best_fitness = numpy.zeros(c.numberOfGenerations)
    for i in range(c.numberOfGenerations):
        best_fitness[i] = -min(phc.fitness[i])
    gen = list(range(c.numberOfGenerations))
    plt.plot(gen, best_fitness)
    plt.xlabel("Generation"); plt.ylabel("Distance traveled")
    plt.title(f"Seed {num}")
    plt.show()