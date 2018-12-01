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

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

ax1.bar(range(len(values)), values, tick_label=individual_nums)

# number of iterations to run
iterations = 1000
count = 0

for i in range(iterations):
    count += 1
    print('iteration:', count) 

    # running redistribution
    pareto.distributor()

    # bar chart
    individual_nums = list(pareto.wealths.keys())
    values = list(pareto.wealths.values())
    ax1.clear()
    ax1.bar(range(len(individual_nums)), values, tick_label=individual_nums, width=1)
    ax1.tick_params(labelsize=8, rotation=90)

    # ordered bar chart
    ax2.clear()
    ax2.bar(range(len(values)), sorted(values), tick_label=individual_nums)

    # wealth distribution histogram
    ax3.clear()
    ax3.hist(list(pareto.wealths.values()))

    plt.pause(0.01)

plt.show()
