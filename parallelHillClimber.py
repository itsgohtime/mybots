from solution import SOLUTION
import numpy
import constants as c
import copy
import os
import random

class PARALLEL_HILL_CLIMBER:
    def __init__(self, seed):
        self.seed = seed
        os.system("del brain*.nndf")
        os.system("del body*.urdf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        self.fitness = numpy.zeros((c.numberOfGenerations, c.populationSize))
        self.gen = 0

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT", self.seed)

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents:
            self.fitness[self.gen, key] = self.parents[key].fitness
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]
        self.gen += 1   

    def Print(self):
        for key in self.parents:
            print('\nComparison of Fitness: \nParent -', self.parents[key].fitness, '\nChild  -', self.children[key].fitness, '\n')

    def Show_Best(self):
        lowest_fitness = 1000
        for key in self.parents:
            if self.parents[key].fitness < lowest_fitness:
                best_solution = self.parents[key]
                lowest_fitness = best_solution.fitness
        #inp = input("\nAre you Ready?")
        print("\n \n The best fitness is:", best_solution.fitness, "\n")
        best_solution.Start_Simulation("GUI", self.seed)
        best_solution.Wait_For_Simulation_To_End()