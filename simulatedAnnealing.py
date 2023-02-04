from solution import SOLUTION
import constants as c
import os
import math
import copy
import random

class SIMULATED_ANNEAL:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del robot_fitness*.txt")
        self.nextAvailableID = 0
        self.T = c.startingTemp
        self.current = SOLUTION(self.nextAvailableID)
        self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.current, "GUI")
        while(self.T != 0):
            for n in range(c.numberofNeighbours):
                self.Random_Successor()
                delta_fitness = self.next.fitness_x - self.current.fitness_x
                if (delta_fitness < 0):
                    self.current = self.next
                else:
                    prob = random.gauss(0.5, 0.5/3)
                    threshold = math.exp(-delta_fitness/(self.T/100))
                    print("\n", self.T, prob, threshold)
                    if (prob < threshold and prob >= 0):
                        self.current = self.next
                print("\n", self.current.fitness_x)
            self.T -= 1
            if (self.current.fitness_x < -7.5):
                self.Show_Best()
        self.Show_Best()

    def Evaluate(self, solution, mode):
        solution.Start_Simulation(mode)
        solution.Wait_For_Simulation_To_End()

    def Random_Successor(self): 
        self.next = copy.deepcopy(self.current)
        self.next.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1
        self.next.Mutate()
        self.Evaluate(self.next, "DIRECT")

    def Show_Best(self):
        lowest_fitness = self.current.fitness_x
        inp = input("Are you Ready?")
        print("The best fitness is:", lowest_fitness)
        self.current.Start_Simulation("GUI")
        self.current.Wait_For_Simulation_To_End()
        exit()