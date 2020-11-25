import random
import math


def random_generator(domain, accuracy_float_points):
    a, z = domain
    if accuracy_float_points == 0:
        return int(random.uniform(a, z))

    return round(random.uniform(a, z), accuracy_float_points)


# def generate_neighbours(point, count, accuracy):
#     neighbours = []
#     for n in range(1, int(count / 2) + 1):
#         neighbour = round(point - (n * accuracy), 2)
#         neighbours.append(neighbour)
#     for n in range(1, int(NEIGHBOUR_COUNT / 2) + 1):
#         neighbour = round(point + (n * accuracy), 2)
#         neighbours.append(neighbour)
#     return neighbours

def generate_neighbours(point, accuracy_float_points_y):
    accuracy = math.pow(10, -accuracy_float_points_y)
    if accuracy_float_points_y == 0:
        neighbours = [int(point - accuracy), int(point + accuracy)]
    else:
        neighbours = [round(point - accuracy, accuracy_float_points_y + 1),
                      round(point + accuracy, accuracy_float_points_y + 1)]
    return neighbours


def count_neigbours(neighbours, function):
    results = []
    for neighbour in neighbours:
        results.append(function(neighbour))
    return results


def hillclimb_xy(function, domain_x, domain_y, attempts, accuracy_float_points_x, accuracy_float_points_y):
    results = []
    current_point_x = random_generator(domain_x, accuracy_float_points_x)
    current_point_y = random_generator(domain_y, accuracy_float_points_y)
    current_result = function(current_point_x, current_point_y)
    for n in range(0, attempts):
        found = False
        neighbours_x = generate_neighbours(current_point_x, accuracy_float_points_x)
        neighbours_y = generate_neighbours(current_point_y, accuracy_float_points_y)
        for neighbour_x in neighbours_x:
            for neighbour_y in neighbours_y:
                if current_result > function(neighbour_x, neighbour_y):
                    current_point_x = neighbour_x
                    current_point_y = neighbour_y
                    current_result = function(current_point_x, current_point_y)
                    found = True
                    results.append(current_result)
                    # print("f(%0.5f, %0.5f) = %0.5f" % (
                    #     current_point_x, current_point_y, function(current_point_x, current_point_y)))
        if found is False:
            print("f(%0.5f, %0.5f) = %0.5f" % (
                current_point_x, current_point_y, current_result))
            print('Znaleziono po', n, 'próbach')
            return results
    return results


def hillclimb_x(function, domain_x, attempts, accuracy_float_points_x, ):
    current_point_x = random_generator(domain_x, accuracy_float_points_x)
    for n in range(0, attempts):
        found = False
        neighbours_x = generate_neighbours(current_point_x, accuracy_float_points_x)
        for neighbour_x in neighbours_x:
            if function(current_point_x) > function(neighbour_x):
                current_point_x = neighbour_x
                found = True
                print("f(%0.2f) = %0.2f" % (current_point_x, function(current_point_x)))
                if found is False:
                    print('Znaleziono po', n, 'próbach')
                    return


def hillclimb(function, domain_x, domain_y, attempts, accuracy_float_points_x, accuracy_float_points_y):
    if domain_y is None:
        return hillclimb_x(function, domain_x, attempts, accuracy_float_points_x)
    else:
        return hillclimb_xy(function, domain_x, domain_y, attempts, accuracy_float_points_x, accuracy_float_points_y)


def hillclimb_xy_random(function, domain_x, domain_y, attempts, accuracy_float_points_x, accuracy_float_points_y):
    results = []
    current_point_x = random_generator(domain_x, accuracy_float_points_x)
    current_point_y = random_generator(domain_y, accuracy_float_points_y)
    current_result = function(current_point_x, current_point_y)
    for n in range(0, attempts):
        neighbour_x = random_generator(domain_x, accuracy_float_points_x)
        neighbour_y = random_generator(domain_y, accuracy_float_points_y)
        neighbour_result = function(neighbour_x, neighbour_y)
        if current_result > neighbour_result:
            current_point_x = neighbour_x
            current_point_y = neighbour_y
            current_result = function(current_point_x, current_point_y)
            results.append(current_result)
            # print("f(%0.5f, %0.5f) = %0.5f" % (
            #     current_point_x, current_point_y, function(current_point_x, current_point_y)))
    print("f(%0.5f, %0.5f) = %0.5f" % (current_point_x, current_point_y, current_result))
    print('Znaleziono po', n, 'próbach')
    return results


def hillclimb_random(function, domain_x, domain_y, attempts, accuracy_float_points_x, accuracy_float_points_y):
    return hillclimb_xy_random(function, domain_x, domain_y, attempts, accuracy_float_points_x,
                               accuracy_float_points_y)
