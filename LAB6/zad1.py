from LAB6.utilis import hillClimbDown
from math import *
import matplotlib.pyplot as plt


def sphere_f(x, n):
    sum = 0
    for i in range(1, n):
        sum += x * x
    return sum


def booth_f(x, y):
    return pow((x + 2 * y - 7), 2) + pow((2 * x + y - 5), 2)


def mc_cormick_f(x, y):
    return sin(x + y) + pow(x - y, 2) - 1.5 * x + 2.5 * y + 1


results = []
for n in range(0, 20):
    result = hillClimbDown(function=mc_cormick_f, domain_x=(-1.5, 4), domain_y=(-3, 4), ATTEMPTS=1000000,
                           ACCURACY_FLOAT_POINTS_X=5, ACCURACY_FLOAT_POINTS_Y=5)
    # result = hillClimbDown(function=booth_f, domain_x=(-10, 10), domain_y=(-10, 10), ATTEMPTS=1000,
    #                        ACCURACY_FLOAT_POINTS_X=0,
    #                        ACCURACY_FLOAT_POINTS_Y=0)

    # result = hillClimbDown(function=sphere_f, domain_x=(-1000, 1000), domain_y=(1, 100), ATTEMPTS=100000,
    #                        ACCURACY_FLOAT_POINTS_X=1, ACCURACY_FLOAT_POINTS_Y=0)
    results.append(result)

for result in results:
    plt.plot(result)
plt.show()
