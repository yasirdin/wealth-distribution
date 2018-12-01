import sys
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
	    # wealth to start with
            self.wealths[val] = 100

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

# instantiating wealthDistributor and providing population
pareto = wealthDistributor(population=100)

individual_nums = list(pareto.wealths.keys())
values = list(pareto.wealths.values())

fig = plt.figure(figsize=(20,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.bar(range(len(values)), values, tick_label=individual_nums)

# number of iterations to run
iterations = 1000
count = 0

for i in range(iterations):
    count += 1
    print('iteration:', count) 

    # running redistribution
    pareto.distributor()
    
    # wealths of each individual in population
    data = pareto.wealths

    # bar chart
    individual_nums = list(pareto.wealths.keys())
    ax1.clear()
    ax1.bar(range(len(data)), list(pareto.wealths.values()), tick_label=individual_nums, width=1)
    ax1.tick_params(labelsize=8, rotation=90)

    # wealth distribution histogram
    ax2.clear()
    ax2.hist(list(pareto.wealths.values()))

    plt.pause(0.1)

plt.show()
