from LAB6.algorithms import hillclimb, hillclimb_random
from LAB6.functions import sphere_f, booth_f, mc_cormick_f
from LAB6.utilis import avg_plot

results_mc_cormick_f_rand = []
results_booth_f_rand = []
results_sphere_f_rand = []
results_mc_cormick_f_hillclimb = []
results_booth_f_hillclimb = []
results_sphere_f_hillclimb = []
for n in range(0, 200):
    results_mc_cormick_f_hillclimb.append(
        hillclimb(function=mc_cormick_f, domain_x=(-1.5, 4), domain_y=(-3, 4), attempts=100000,
                  accuracy_float_points_x=5, accuracy_float_points_y=5))
    results_booth_f_hillclimb.append(
        hillclimb(function=booth_f, domain_x=(-10, 10), domain_y=(-10, 10), attempts=10000,
                  accuracy_float_points_x=0, accuracy_float_points_y=0))

    results_sphere_f_hillclimb.append(
        hillclimb(function=sphere_f, domain_x=(-1000, 1000), domain_y=(1, 100), attempts=100000,
                  accuracy_float_points_x=1, accuracy_float_points_y=0))
    results_mc_cormick_f_rand.append(
        hillclimb_random(function=mc_cormick_f, domain_x=(-1.5, 4), domain_y=(-3, 4), attempts=100000,
                         accuracy_float_points_x=5, accuracy_float_points_y=5))
    results_booth_f_rand.append(
        hillclimb_random(function=booth_f, domain_x=(-10, 10), domain_y=(-10, 10), attempts=10000,
                         accuracy_float_points_x=0,
                         accuracy_float_points_y=0))

    results_sphere_f_rand.append(
        hillclimb_random(function=sphere_f, domain_x=(-1000, 1000), domain_y=(1, 100), attempts=100000,
                         accuracy_float_points_x=1, accuracy_float_points_y=0))

avg_plot(results_mc_cormick_f_hillclimb, 'results_mc_cormick_f HILLCLIMB')
avg_plot(results_booth_f_hillclimb, 'results_booth_f HILLCLIMB')
avg_plot(results_sphere_f_hillclimb, 'results_sphere_f HILLCLIMB')
avg_plot(results_mc_cormick_f_rand, 'results_mc_cormick_f RAND')
avg_plot(results_booth_f_rand, 'results_booth_f RAND')
avg_plot(results_sphere_f_rand, 'results_sphere_f RAND')
