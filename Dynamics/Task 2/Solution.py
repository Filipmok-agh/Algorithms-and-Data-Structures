from zad8testy import runtests
from math import inf

# The function calculates the optimal distance from the first parking space to the last building.
# The algorithm works using dynamic programming. For each parking space in a given building, it computes
# the distance to the parking space of the previous building while updating the best possible distance,
# considering previous calculations for other parking spaces. Finally, it returns the minimal distance
# to the last building and parking space.
# Time complexity is:  O(n * m)

def find_optimal_parking_distance(buildings, parking_spaces):
    num_buildings = len(buildings)
    num_parking_spaces = len(parking_spaces)
    
    distance = [[inf for _ in range(num_buildings)] for _ in range(num_parking_spaces)]
    best_distance = [[inf for _ in range(num_buildings)] for _ in range(num_parking_spaces)]
    
    best_distance[0][0] = abs(parking_spaces[0] - buildings[0])
    distance[0][0] = best_distance[0][0]
    
    for i in range(1, num_parking_spaces):
        distance[i][0] = abs(parking_spaces[i] - buildings[0])
        best_distance[i][0] = min(distance[i][0], best_distance[i-1][0])
    
    for i in range(1, num_buildings):
        for j in range(i, num_parking_spaces):
            distance[j][i] = best_distance[j-1][i-1] + abs(parking_spaces[j] - buildings[i])
            best_distance[j][i] = min(distance[j][i], best_distance[j-1][i])
    
    return best_distance[num_parking_spaces - 1][num_buildings - 1]

runtests(find_optimal_parking_distance, all_tests=True)
input("Press Enter to exit...")

