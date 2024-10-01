"""
Napisać algorytm, który przyjmuje jako argyment jednowymiarową tablicę liczb. Pierwsza liczba z tablicy przyjmuje dowolną wartość
całkowitą zaś reszta elementów tablicy to liczby należace do zbioru {1, 0}. Jeden oznacza, że dane miejsce może być 'źródłem'
zaś 0 oznacza, że nie może nim być. Alogorytm ma zwracać minimalną liczbę źródeł w dozowlonych pozycjach dla, których
każdy element tablicy jest połączony ze źródłem. Pierwsza liczba z tablicy oznacza maksymalną długośc połączenia w jednostakch.
Elementy tablicy są oddalone o jednostkę. W przypadku braku możliwości połączenia każdego elementu tablicy do źródła
algorytm powinien zwracać -1.
"""
import random
from itertools import combinations


def power_outlets(arr):
# Extract K from input and extract list of desks.
# Calculate number of desks and get list of desks that can have an outlet.
    k = arr[0]
    desks = arr[1:]
    num_desks = len(desks)
    power_desks = []
    for i in range(0, num_desks):
        if desks[i] == 1:
            power_desks.append(i)

    possible_configs = []
    # Function below calcultes minimal number of outlets. If with given array all desks can't be connected to outlets
    # returns -1. Function checks the differance between index of desks with outlets ('power outlets') and checks if
    #for all desks the distance is smaller or equal k.
    def optimize_power_outlets():
        possible = False
        for n in range(1, len(power_desks) + 1):
            if n == 1:
                for index in power_desks:
                    # set index of the outlet
                    power_index = index
                    reachable = 0
                    # for each desk calculate distance to the outlet
                    for i in range(0,len(desks)):
                        dist = abs(i - power_index)
                        if dist <= k:
                            reachable += 1
                        else:
                            pass
                    if reachable == len(desks):
                        result = power_index
                        return n
                    else:
                        pass
            else:
                # Create list of all posisible combinations of lenght n.
                configs = list(combinations(power_desks, n))
                for config in configs:
                    # set indices of desks with outlets.
                    power_indices = []
                    reachable_desks = 0
                    for i in config:
                        power_indices.append(i)
                    distances = []
                    minimal_distances =[]
                    # The rest of the script calculates distance for every desks to the nearest outlet. Generally it's similar to the
                    # part with n = 1.
                    for i in range(0, len(desks)):
                        for index in power_indices:
                            distance = abs(i - index)
                            distances.append(distance)
                        minimal_distance = min(distances)
                        distances = []
                        minimal_distances.append(minimal_distance)
                    for min_dist in minimal_distances:
                        if min_dist <= k:
                            reachable_desks += 1
                    if reachable_desks == len(desks) :
                        possible = True
                        return n
                    else:
                        pass
        if possible == False:
            return -1

    resulting = optimize_power_outlets()
    return resulting

# create random list for the input to the function
random_list = []
n = 0
for i in range(0, 50):
    if n == 0:
        random_list.append(random.randint(1, 5))
        n += 1
    else:
        random_list.append(random.randint(0,1))

print(random_list)
print(power_outlets(random_list))
