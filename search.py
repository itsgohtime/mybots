import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import time
import matplotlib.pyplot as plt
import constants as c
import numpy
import random

print("\n")
#os.system("del best_robots")
for num in [3]:
    random.seed(num)
    numpy.random.seed(num)
    num = random.randint(0,100)
    phc = PARALLEL_HILL_CLIMBER(num)
    phc.Evolve()
    phc.Show_Best()
    best_fitness = numpy.zeros(c.numberOfGenerations)
    for i in range(c.numberOfGenerations):
        best_fitness[i] = -min(phc.fitness[i])
    gen = list(range(c.numberOfGenerations))
    plt.plot(gen, best_fitness, label = f"Seed {num}")
plt.xlabel("Generation"); plt.ylabel("Distance traveled")
plt.title("Fitness Curves"); plt.legend()
plt.show()