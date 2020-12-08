from LAB9.evolution import generate_genotype, genotype_to_xy, xy_to_genotype, generate_population, cross, \
    find_random_alg, mutate, selection, fitness_population
import LAB9.functions as f
import matplotlib.pyplot as plt


def test_gray_binary_xy():
    accuracy_x = 2
    accuracy_y = 2
    size = 20

    genotype = generate_genotype(size=size)
    print(genotype)
    x, y = genotype_to_xy(genotype=genotype, accuracy_x=accuracy_x, accuracy_y=accuracy_x)
    print(x, y)

    gentotype_prim = xy_to_genotype(x=x, y=y, size=size, accuracy_x=accuracy_x, accuracy_y=accuracy_y)
    print(gentotype_prim)
    print(genotype == gentotype_prim)


def find_random():
    accuracy_x = 2
    accuracy_y = 2
    size = 20
    genotype, results = find_random_alg(f.himmelblau_f, 10000, size, accuracy_x, accuracy_y)
    print(genotype_to_xy(genotype, accuracy_x, accuracy_y))
    plt.plot(results)
    plt.title('random genotype himmelblau attempts=10.000.000')
    plt.show()


def test_cross():
    size = 20
    genotype1 = generate_genotype(size=size)
    genotype2 = generate_genotype(size=size)
    print(genotype1, genotype2)
    new_genotype1, new_genotype2 = cross(genotype1, genotype2)
    print(new_genotype1, new_genotype2)


def test_mutation():
    size = 20
    genotype = generate_genotype(size=size)
    print(genotype)
    mutated_genotype = mutate(genotype, 1)
    print(mutated_genotype)


def test_selection():
    population = generate_population(100, 20)
    print('Primary fitness: ', fitness_population(f.himmelblau_f, population))

    for i in range(0, 100):
        if i == 0:
            new_population = selection(population, f.himmelblau_f)
        else:
            new_population = selection(new_population, f.himmelblau_f)
        print(i, fitness_population(f.himmelblau_f, new_population))


# test_gray_binary_xy()
# find_random()
# test_cross()
# test_mutation()
# test_selection()
