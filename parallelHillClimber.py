from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        #self.parent = SOLUTION()

    def Evolve(self):
        self.Evaluate(self.parents)
        # self.parent.Evaluate("GUI")
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
        # self.child = copy.deepcopy(self.parent)
        # self.child.Set_ID(self.nextAvailableID)
        
    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()
        # self.child.Mutate()

    def Evaluate(self, solutions):
        for i in range(c.populationSize):
            solutions[i].Start_Simulation("DIRECT")

        for i in range(c.populationSize):
            solutions[i].Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        for key in self.parents:
            print('\nComparison of Fitness: \nParent -', self.parents[key].fitness, '\nChild  -', self.children[key].fitness, '\n')

    def Show_Best(self):
        lowest_fitness = 1000
        for key in self.parents:
            if self.parents[key].fitness < lowest_fitness:
                best_solution = self.parents[key]
                lowest_fitness = best_solution.fitness
        print("The best fitness is:", best_solution.fitness)
        best_solution.Start_Simulation("GUI")
        best_solution.Wait_For_Simulation_To_End()
        # self.parent.Evaluate("GUI")   