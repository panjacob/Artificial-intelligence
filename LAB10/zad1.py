from LAB10.evolution import generate_population, selection_tournament, cross_population, mutate_population, find_elite, \
    select_better, keep_elite_in_population
import LAB10.functions as f
import matplotlib.pyplot as plt


def genetic(size_of_population, size_arr, function, mutate_probability, elite_count, iterations):
    population = generate_population(size_of_population, size_arr)
    elite = find_elite(population, function, elite_count)
    plot = [elite[0][0]]
    # print(0, " : ", round(elite[0][0], 2))

    for i in range(iterations):
        population = selection_tournament(population, function)
        population = cross_population(population, 0.1)
        population = mutate_population(population, mutate_probability)
        new_elite = find_elite(population, function, elite_count)
        elite = select_better(elite, new_elite)
        population = keep_elite_in_population(elite, population)
        # print(i, " : ", round(elite[0][0], 2))
        plot.append(elite[0][0])
    return elite[0], plot


solution, plot = genetic(size_of_population=100, size_arr=20, function=f.himmelblau_f, mutate_probability=1,
                         elite_count=3,
                         iterations=1000)

plt.plot(plot)
plt.title('genetic alg')
plt.show()
