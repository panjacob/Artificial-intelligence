from LAB8.utilis import random_binary, binary_to_gray, gray_to_binary, split_half, divide_value_to_accuracy, \
    binary_to_10, int_to_bin


def generate_genotype(size=128):
    binary = []
    for i in range(0, size):
        binary.append(random_binary())
    # print('b1', binary)
    return binary_to_gray(binary)


def genotype_to_xy(genotype, accuracy_x=0, accuracy_y=0):
    binary = gray_to_binary(genotype)
    first_half_gray, second_half_gray = split_half(binary)
    first_half = gray_to_binary(first_half_gray)
    second_half = gray_to_binary(second_half_gray)
    # print(first_half, second_half)
    x = binary_to_10(first_half)
    # print(x)
    y = binary_to_10(second_half)
    x = divide_value_to_accuracy(x, accuracy_x)
    y = divide_value_to_accuracy(y, accuracy_y)
    return x, y


def xy_to_genotype(x, y, size=128):
    first_half_str = int_to_bin(x, size)
    second_half_str = int_to_bin(y, size)

    binary = []
    for char in first_half_str + second_half_str:
        binary.append(int(char))
    return binary_to_gray(binary)


def fitness_to_zero(function, genotype):
    x, y = genotype_to_xy(genotype)
    f_result = function(x, y)
    return 1 / abs(f_result)
