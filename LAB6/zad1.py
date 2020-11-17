import random
import numpy as np


def sphere_f(x, n):
    sum = 0
    for i in range(1, n):
        sum += pow(x, 2)
    return sum


def randomGeneratorInt():
    a = -10000
    b = 10000
    return random.randint(a, b)


def find_neighbours(x, begin,end, accuracy):
    # linespace
    neighbours = np.arange(begin,end, accuracy)
    return neighbours.tolist()


def hillClimbRandMin(function, randomGenerator, attempts):
    lowest = 9999
    for n in range(0, attempts):
        current = function(1, n)
        if current <= lowest:
            lowest = current
            print("attepmt: " + str(n) + "  val: " + str(lowest))
    print(lowest)



x = find_neighbours(10, -5,5, 0.1)
print(x)
