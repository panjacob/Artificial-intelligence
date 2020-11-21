import random
import math


def random_generator(domain, ACCURACY_FLOAT_POINTS):
    a, z = domain
    if ACCURACY_FLOAT_POINTS == 0:
        return int(random.uniform(a, z))

    return round(random.uniform(a, z), ACCURACY_FLOAT_POINTS)


# def generate_neighbours(point, count, accuracy):
#     neighbours = []
#     for n in range(1, int(count / 2) + 1):
#         neighbour = round(point - (n * accuracy), 2)
#         neighbours.append(neighbour)
#     for n in range(1, int(NEIGHBOUR_COUNT / 2) + 1):
#         neighbour = round(point + (n * accuracy), 2)
#         neighbours.append(neighbour)
#     return neighbours

def generate_neighbours(point, ACCURACY_FLOAT_POINTS):
    accuracy = math.pow(10, -ACCURACY_FLOAT_POINTS)
    if ACCURACY_FLOAT_POINTS == 0:
        neighbours = [int(point - accuracy), int(point + accuracy)]
    else:
        neighbours = [round(point - accuracy, ACCURACY_FLOAT_POINTS + 1),
                      round(point + accuracy, ACCURACY_FLOAT_POINTS + 1)]
    return neighbours


def count_neigbours(neighbours, function):
    results = []
    for neighbour in neighbours:
        results.append(function(neighbour))
    return results


# def hillClimbDown(function, domain_x, domain_y, ATTEMPTS, ACCURACY_FLOAT_POINTS_X, ACCURACY_FLOAT_POINTS_Y):
#     current_point_x = random_generator(domain_x, ACCURACY_FLOAT_POINTS_X)
#     if domain_y is not None:
#         current_point_y = random_generator(domain_y, ACCURACY_FLOAT_POINTS_Y)
#     print('Start na:', current_point_x)
#     for n in range(0, ATTEMPTS):
#         found = False
#         neighbours_x = generate_neighbours(current_point_x, ACCURACY_FLOAT_POINTS_X)
#         if domain_y is not None:
#             neighbours_y = generate_neighbours(current_point_y, ACCURACY_FLOAT_POINTS_Y)
#
#         for neighbour_x in neighbours_x:
#             if function(current_point_x) >= function(neighbour_x):
#                 current_point_x = neighbour_x
#                 found = True
#         if found is False:
#             print('Znaleziono po', n, 'próbach')
#             return current_point_x
#         # print(current_point)
#     return current_point_x


def hillClimbDownXY(function, domain_x, domain_y, ATTEMPTS, ACCURACY_FLOAT_POINTS_X, ACCURACY_FLOAT_POINTS_Y):
    results = []
    current_point_x = random_generator(domain_x, ACCURACY_FLOAT_POINTS_X)
    current_point_y = random_generator(domain_y, ACCURACY_FLOAT_POINTS_Y)
    for n in range(0, ATTEMPTS):
        found = False
        neighbours_x = generate_neighbours(current_point_x, ACCURACY_FLOAT_POINTS_X)
        neighbours_y = generate_neighbours(current_point_y, ACCURACY_FLOAT_POINTS_Y)
        current_result = function(current_point_x, current_point_y)
        for neighbour_x in neighbours_x:
            for neighbour_y in neighbours_y:
                if current_result > function(neighbour_x, neighbour_y):
                    current_point_x = neighbour_x
                    current_point_y = neighbour_y
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


def hillClimbDownX(function, domain_x, ATTEMPTS, ACCURACY_FLOAT_POINTS_X, ):
    current_point_x = random_generator(domain_x, ACCURACY_FLOAT_POINTS_X)
    for n in range(0, ATTEMPTS):
        found = False
        neighbours_x = generate_neighbours(current_point_x, ACCURACY_FLOAT_POINTS_X)
        for neighbour_x in neighbours_x:
            if function(current_point_x) > function(neighbour_x):
                current_point_x = neighbour_x
                found = True
                print("f(%0.2f) = %0.2f" % (current_point_x, function(current_point_x)))
                if found is False:
                    print('Znaleziono po', n, 'próbach')
                    return


def hillClimbDown(function, domain_x, domain_y, ATTEMPTS, ACCURACY_FLOAT_POINTS_X, ACCURACY_FLOAT_POINTS_Y):
    if domain_y is None:
        return hillClimbDownX(function, domain_x, ATTEMPTS, ACCURACY_FLOAT_POINTS_X)
    else:
        return hillClimbDownXY(function, domain_x, domain_y, ATTEMPTS, ACCURACY_FLOAT_POINTS_X, ACCURACY_FLOAT_POINTS_Y)
