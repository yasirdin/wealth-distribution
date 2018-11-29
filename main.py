import numpy as np
import matplotlib.pyplot as plt
import time
import random

class wealthDistributor():
    def __init__(self, population):
        self.population = population
        
        # wealth at time=0
        self.wealths = {}
        for val in np.arange(0, self.population):
            self.wealths[val] = 1

    def distributor(self):
        """this function will run redistribution of wealth"""
        # random_ints = [random.randint(0, self.population) for i in range(100)]
        random_selections = []
        for key, value in self.wealths.items():
            if value==0:
                pass
            else:
                self.wealths[key] = value - 1
                random_selections.append(random.randint(0, self.population-1))

        # giving coins to randomly selected
        for val in random_selections:
            wealth = self.wealths[val]
            self.wealths[val] = wealth + 1

# instantiating wealthDistributor:
pareto = wealthDistributor(population=1000)

iterations = 1000

for i in range(iterations):
    # run redistribution
    pareto.distributor()
    
    plt.clf()
    # wealths of each individual in population
    x = pareto.wealths.values()
    plt.hist(x)
    plt.pause(0.25)

plt.show()
    
    # time.sleep(1)

