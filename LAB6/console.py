import sys
from algorithms import hillclimb, hillclimb_random
from functions import sphere_f, booth_f, mc_cormick_f
from utilis import avg_plot

# python LAB6/console.py algorithm=hillclimb function=sphere_f domain_x=-1000,1000 domain_y=1,100 attempts=100000 accuracy_float_points_x=0 accuracy_float_points_y=0 repeat=2000
# python LAB6/console.py algorithm=hillclimb function=booth_f domain_x=-10,10 domain_y=10,10 attempts=100000 accuracy_float_points_x=1 accuracy_float_points_y=0 repeat=200
arguments = []
for arg in sys.argv[1:]:
    arguments.append(arg.split('='))

algorithm = None
function = None
repeat = 1
description = ""
for arg, val in arguments:
    if arg == 'algorithm':
        description += val
        if val == 'hillclimb':
            algorithm = hillclimb
        elif val == 'random':
            algorithm = hillclimb
        else:
            algorithm = hillclimb
    if arg == 'function':
        description += val
        if val == 'sphere_f':
            function = sphere_f
        elif val == 'booth_f':
            function = booth_f
        elif val == 'mc_cormick_f':
            function = mc_cormick_f
        else:
            function = sphere_f
    if arg == 'domain_x':
        a, z = val.split(',')
        domain_x = (float(a), float(z))
    if arg == 'domain_y':
        a, z = val.split(',')
        domain_y = (float(a), float(z))
    if arg == 'attempts':
        attempts = int(val)
    if arg == 'accuracy_float_points_x':
        accuracy_float_points_x = int(val)
    if arg == 'accuracy_float_points_y':
        accuracy_float_points_y = int(val)
    if arg == 'repeat':
        repeat = int(val)

results = []
for n in range(0, repeat):
    results.append(
        algorithm(function=function, domain_x=domain_x, domain_y=domain_y, attempts=attempts,
                  accuracy_float_points_x=accuracy_float_points_x, accuracy_float_points_y=accuracy_float_points_y))

avg_plot(results, description)
