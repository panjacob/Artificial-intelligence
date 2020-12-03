from LAB8.utilis import random_binary, binary_to_gray, gray_to_binary, split_half, divide_value_to_accuracy, \
    binary_to_10, int_to_bin, normal_to_plusminus, plusminus_to_normal


def generate_genotype(size):
    binary = []
    for i in range(0, size):
        binary.append(random_binary())
    return binary_to_gray(binary)


def generate_population(size_of_population, size):
    population = []
    for i in range(0, size_of_population):
        population.append(generate_genotype(size))
    return population


def genotype_to_xy(genotype, size, accuracy_x=0, accuracy_y=0):
    binary = gray_to_binary(genotype)
    first_half, second_half = split_half(binary)
    x = binary_to_10(first_half)
    y = binary_to_10(second_half)
    x = divide_value_to_accuracy(x, accuracy_x)
    y = divide_value_to_accuracy(y, accuracy_y)
    x = normal_to_plusminus(x, size, accuracy_x)
    y = normal_to_plusminus(y, size, accuracy_y)
    return x, y


def xy_to_genotype(x, y, accuracy_x, accuracy_y, size):
    x = plusminus_to_normal(x, size, accuracy_x)
    y = plusminus_to_normal(y, size, accuracy_y)
    first_half_str = int_to_bin(x, accuracy_x, size)
    second_half_str = int_to_bin(y, accuracy_y, size)
    binary = []
    for char in first_half_str + second_half_str:
        binary.append(int(char))
    return binary_to_gray(binary)


def fitness(function, genotype, size, accuracy_x, accuracy_y, aim=0):
    x, y = genotype_to_xy(genotype, size, accuracy_x, accuracy_y)
    f_result = function(x, y)
    result = 1 / abs(aim - f_result)
    # return round(result, 10)
    return result


def monte_carlo(function, iterations, size, accuracy_x, accuracy_y):
    results = []
    current_genotype = generate_genotype(size)
    current_fitness = fitness(function, current_genotype, size, accuracy_x, accuracy_y)
    for i in range(0, iterations):
        next_genotype = generate_genotype(size)
        next_fitness = fitness(function, next_genotype, size, accuracy_x, accuracy_y)
        if current_fitness < next_fitness:
            current_genotype = next_genotype
            current_fitness = next_fitness
        results.append(current_fitness)
    return current_genotype, results
