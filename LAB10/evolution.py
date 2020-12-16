from LAB10.utilis import random_binary, binary_to_gray, gray_to_binary, split_half, divide_value_to_accuracy, \
    binary_to_10, int_to_bin, normal_to_plusminus, plusminus_to_normal, random_float_0_1, random_int, invert_bin, \
    random_choice_2


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


def genotype_to_xy(genotype, accuracy_x=0, accuracy_y=0):
    size = len(genotype)
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


def fitness(function, genotype, accuracy_x, accuracy_y, aim=0):
    x, y = genotype_to_xy(genotype, accuracy_x, accuracy_y)
    f_result = function(x, y)
    result = 1 / abs(aim - f_result)
    # return round(result, 10)
    return result


def fitness_population(function, population, accuracy_x=2, accuracy_y=2, aim=0):
    overall_fitness = 0
    for genotype in population:
        overall_fitness += fitness(function, genotype, accuracy_x, accuracy_y, aim)
    return overall_fitness


# def fintess_best_in_population(function, population, accuracy_x=2, accuracy_y=2, aim=0):
#     best_fitness = -9999
#     best_genotype = None
#     for genotype in population:
#         current_fitness = fitness(function, genotype, accuracy_x, accuracy_y, aim)
#         if current_fitness > best_fitness:
#             best_fitness = current_fitness
#             best_genotype = genotype
#     return best_genotype, best_fitness


def fitness_every_genotype(population, function, accuracy_x, accuracy_y, aim):
    result = {}
    for i in range(len(population)):
        result[i] = fitness(function, population[i], accuracy_x, accuracy_y, aim)
    return result


def sort_calculated_population(calculated_population):
    return dict(sorted(calculated_population.items(), key=lambda item: item[1], reverse=True))


def find_elite(population, function, count, accuracy_x=2, accuracy_y=2, aim=0):
    calculated_population = fitness_every_genotype(population, function, accuracy_x, accuracy_y, aim)
    calculated_population_sorted = sort_calculated_population(calculated_population)
    # print(calculated_population_sorted)
    elite = []
    for i in range(0, count):
        key = list(calculated_population_sorted.keys())[i]
        value = calculated_population_sorted[key]
        genotype = population[key]
        elite.append((value, genotype))
    return elite


def keep_elite_in_population(elite, population):
    for e in elite:
        while e[1] not in population:
            population.pop(0)
            population.append(e[1])
    return population

    # for e in elite:
    #     if e[1] not in population:
    #         print('ERRROORRR!!!')
    # return population


def select_better(elite1, elite2):
    length = len(elite1)
    elite_connected = elite1 + elite2
    elite_sorted = sorted(elite_connected, key=lambda x: x[0], reverse=True)
    return elite_sorted[:length]


def find_random_alg(function, iterations, size, accuracy_x, accuracy_y):
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


def cross(genotype1, genotype2):
    genotype1_1, genotype1_2 = split_half(genotype1)
    genotype2_1, genotype2_2 = split_half(genotype2)
    new_genotype_1 = genotype1_1 + genotype2_2
    new_genotype_2 = genotype2_1 + genotype1_2
    return new_genotype_1, new_genotype_2


def mutate(genotype, probability):
    if probability >= random_float_0_1():
        pos_bit_to_change = random_int(0, len(genotype) - 1)
        # print('mutuję na pozycji: ' + str(pos_bit_to_change))
        genotype[pos_bit_to_change] = invert_bin(genotype[pos_bit_to_change])
    return genotype


def selection_tournament(population, function, accuracy_x=2, accuracy_y=2, aim=0):
    population_len = len(population)
    new_population = []
    for i in range(0, population_len):
        genotype1, genotype2 = random_choice_2(population)
        fit1 = fitness(function, genotype1, accuracy_x, accuracy_y, aim)
        fit2 = fitness(function, genotype2, accuracy_x, accuracy_y, aim)
        if fit1 > fit2:
            new_population.append(genotype1)
        else:
            new_population.append(genotype2)
    return new_population


def cross_population(population, probability):
    new_population = []
    half_size_population = int(len(population) / 2)
    for x in range(half_size_population):
        genotype1, genotype2 = random_choice_2(population)
        if probability >= random_float_0_1():
            new_genotype1, new_genotype2 = cross(genotype1, genotype2)
            new_population.append(new_genotype1)
            new_population.append(new_genotype2)
        else:
            new_population.append(genotype1)
            new_population.append(genotype2)
    return new_population


def mutate_population(population, probability):
    for i in range(0, len(population)):
        population[i] = mutate(population[i], probability)
    return population
