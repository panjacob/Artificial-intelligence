import random


def xor(a, b):
    return int(bool(a) ^ bool(b))


def binary_to_gray(binary):
    gray = [binary[0]]

    for i in range(1, len(binary)):
        previous = binary[i - 1]
        current = binary[i]
        # print(previous, current, " = ", xor(current, previous))
        result = xor(current, previous)
        gray.append(result)

    return gray


def gray_to_binary(gray):
    binary = [gray[0]]

    for i in range(1, len(gray)):
        previous = binary[i - 1]
        current = gray[i]
        # print(previous, current, " = ", xor(current, previous))
        result = xor(current, previous)
        binary.append(result)

    return binary


def random_binary():
    return random.randint(0, 1)


def split_half(arr):
    middle_index = int(len(arr) / 2)
    first_half = arr[:middle_index]
    second_half = arr[middle_index:]
    return first_half, second_half


def binary_to_10(binary):
    result = 0
    for i, bit in enumerate(reversed(binary)):
        result += bit * int(pow(2, i))
        # print(bit, ' * ', pow(2, i) , ' = ', bit * int(pow(2, i)))
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
        # print(binary)
    return binary


def int_to_bin(x, size=128):
    binary = str(bin(x))[2:]
    # print(binary, ' -> ', binary_fill_zeros(binary, size))
    return binary_fill_zeros(binary, size)
