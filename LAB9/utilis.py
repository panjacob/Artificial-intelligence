import random


def xor(a, b):
    return int(bool(a) ^ bool(b))


def binary_to_gray(binary):
    gray = [binary[0]]

    for i in range(1, len(binary)):
        previous = binary[i - 1]
        current = binary[i]
        result = xor(current, previous)
        gray.append(result)

    return gray


def gray_to_binary(gray):
    binary = [gray[0]]

    for i in range(1, len(gray)):
        previous = binary[i - 1]
        current = gray[i]
        result = xor(current, previous)
        binary.append(result)

    return binary


def random_binary():
    return random.randint(0, 1)


def random_float_0_1():
    return random.uniform(0, 1)


def random_int(a, b):
    return random.randint(a, b)


def split_half(arr):
    middle_index = int(len(arr) / 2)
    first_half = arr[:middle_index]
    second_half = arr[middle_index:]
    return first_half, second_half


def binary_to_10(binary):
    result = 0
    for i, bit in enumerate(reversed(binary)):
        result += bit * int(pow(2, i))
    return result


def divide_value_to_accuracy(value, accuracy):
    if accuracy != 0:
        return value / pow(10, accuracy)
    else:
        return value


def binary_fill_zeros(binary, size=128):
    size = int(size / 2)
    while len(binary) != size:
        binary = '0' + binary
    return binary


def int_to_bin(x, accuracy, size=128):
    x = int(x * pow(10, accuracy))
    binary = str(bin(x))[2:]
    return binary_fill_zeros(binary, size)


def normal_to_plusminus(x, size, accuracy):
    max_val = pow(2, size / 2) / pow(10, accuracy)
    middle = max_val / 2
    if x < middle:
        if x == 0:
            return 0
        return -1 * x
    else:
        return x - middle


def plusminus_to_normal(x, size, accuracy):
    max_val = pow(2, size / 2) / pow(10, accuracy)
    middle = max_val / 2
    if x < 0:
        return -1 * x
    else:
        return x + middle


def invert_bin(bin):
    if bin == 1:
        return 0
    else:
        return 1


def random_choice_2(population):
    return random.choice(population), random.choice(population)


