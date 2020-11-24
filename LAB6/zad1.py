from LAB6.utilis import hillClimbDown
from LAB6.randutilis import hillClimbDown_rand
from math import *
import matplotlib.pyplot as plt


def avg_plot(results, title):
    sum = []
    for result in results:
        for i, el in enumerate(result):
            if len(sum) > i:
                sum[i] += el
            else:
                sum.append(el)
        # plt.plot(result)
    plt.plot(sum)
    plt.title(title)
    plt.show()


def sphere_f(x, n):
    sum = 0
    for i in range(1, n):
        sum += x * x
    return sum


def booth_f(x, y):
    return pow((x + 2 * y - 7), 2) + pow((2 * x + y - 5), 2)


def mc_cormick_f(x, y):
    return sin(x + y) + pow(x - y, 2) - 1.5 * x + 2.5 * y + 1


results_mc_cormick_f = []
results_booth_f = []
results_sphere_f = []
for n in range(0, 20):
    results_mc_cormick_f.append(
        hillClimbDown_rand(function=mc_cormick_f, domain_x=(-1.5, 4), domain_y=(-3, 4), ATTEMPTS=100000,
                           ACCURACY_FLOAT_POINTS_X=5, ACCURACY_FLOAT_POINTS_Y=5))
    results_booth_f.append(hillClimbDown_rand(function=booth_f, domain_x=(-10, 10), domain_y=(-10, 10), ATTEMPTS=1000,
                                              ACCURACY_FLOAT_POINTS_X=0,
                                              ACCURACY_FLOAT_POINTS_Y=0))

    results_sphere_f.append(
        hillClimbDown_rand(function=sphere_f, domain_x=(-1000, 1000), domain_y=(1, 100), ATTEMPTS=100000,
                           ACCURACY_FLOAT_POINTS_X=1, ACCURACY_FLOAT_POINTS_Y=0))

avg_plot(results_mc_cormick_f, 'results_mc_cormick_f RAND')
avg_plot(results_booth_f, 'results_booth_f RAND')
avg_plot(results_sphere_f, 'results_sphere_f RAND')

results_mc_cormick_f = []
results_booth_f = []
results_sphere_f = []
for n in range(0, 20):
    results_mc_cormick_f.append(
        hillClimbDown(function=mc_cormick_f, domain_x=(-1.5, 4), domain_y=(-3, 4), ATTEMPTS=100000,
                      ACCURACY_FLOAT_POINTS_X=5, ACCURACY_FLOAT_POINTS_Y=5))
    results_booth_f.append(
        hillClimbDown(function=booth_f, domain_x=(-10, 10), domain_y=(-10, 10), ATTEMPTS=1000,
                      ACCURACY_FLOAT_POINTS_X=0, ACCURACY_FLOAT_POINTS_Y=0))

    results_sphere_f.append(
        hillClimbDown(function=sphere_f, domain_x=(-1000, 1000), domain_y=(1, 100), ATTEMPTS=100000,
                      ACCURACY_FLOAT_POINTS_X=1, ACCURACY_FLOAT_POINTS_Y=0))

avg_plot(results_mc_cormick_f, 'results_mc_cormick_f HILLCLIMB')
avg_plot(results_booth_f, 'results_booth_f HILLCLIMB')
avg_plot(results_sphere_f, 'results_sphere_f HILLCLIMB')
