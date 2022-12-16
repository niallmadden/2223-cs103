import random
import matplotlib.pyplot as plt

# Histogram code from Week 10
def histogram(my_list):
    """Creates a histogram of items in my_list. Returns a dictionary, 
    where d[key] is the frequency of key in the list"""
    d = dict()
    for element in my_list:
        if element not in d:
            d[element] = 1
        else:
            d[element] += 1
        # print(d)
    return d

# plot_historam() from Week 10
def plot_histogram(d):
    """ plot histogram data stored in dictionary d """
    plt.bar( list(d.keys()), list(d.values()))

# VarioDie from Week 11 (with __str__ added)
class VarioDie: 
    """ Make an n-sided die. n=6 by default"""
    def __init__(self, sides=6): # two underscores on each side!
        self.sides = sides
        self.value = 1
        
    def roll(self):
        self.value = random.randint(1, self.sides)
        
    def __str__(self):
        return f"{self.value}"
    
    
    
