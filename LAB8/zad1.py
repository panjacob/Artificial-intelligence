from LAB8.evolution import generate_genotype, genotype_to_xy, xy_to_genotype, generate_population, fitness, monte_carlo
import LAB8.functions as f
import matplotlib.pyplot as plt


def test1():
    accuracy_x = 2
    accuracy_y = 2
    size = 20

    genotype = generate_genotype(size=size)
    print(genotype)
    x, y = genotype_to_xy(genotype=genotype, size=size, accuracy_x=accuracy_x, accuracy_y=accuracy_x)
    print(x, y)

    gentotype_prim = xy_to_genotype(x=x, y=y, size=size, accuracy_x=accuracy_x, accuracy_y=accuracy_y)
    print(gentotype_prim)
    print(genotype == gentotype_prim)


def find_random():
    accuracy_x = 2
    accuracy_y = 2
    size = 20
    genotype, results = monte_carlo(f.himmelblau_f, 10000000, size, accuracy_x, accuracy_y)
    print(genotype_to_xy(genotype, size, accuracy_x, accuracy_y))
    plt.plot(results)
    plt.title('random genotype himmelblau attempts=10.000.000')
    plt.show()

test1()
find_random()
