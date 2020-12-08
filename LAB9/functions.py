from math import *


def sphere_f(x, n):
    sum = 0
    for i in range(1, n):
        sum += x * x
    return sum


def booth_f(x, y):
    return pow((x + 2 * y - 7), 2) + pow((2 * x + y - 5), 2)


def mc_cormick_f(x, y):
    return sin(x + y) + pow(x - y, 2) - 1.5 * x + 2.5 * y + 1


def himmelblau_f(x, y):
    return pow(pow(x, 2) + y - 11, 2) + pow(x + pow(y, 2) - 7, 2)

