from zad9testy import runtests
from queue import PriorityQueue

# The algorithm inserts all the values from the matrix into a priority queue and then checks if it's possible
# to increase the value of a field by examining the neighboring fields. The algorithm then updates the distance 
# of the current cell based on the best possible value from its neighbors. The result is the best distance for 
# the last cell in the priority queue.
# Time complexity: O(n * m * log(n * m))

def trip(M):
    n = len(M)
    m = len(M[0])
    Q = PriorityQueue()

    for i in range(n):
        for j in range(m):
            Q.put((M[i][j], i, j))

    dist = [[1 for _ in range(m)] for _ in range(n)]

    def mostoptimal(val, i, j):
        best = 0
        if i - 1 >= 0:
            if M[i - 1][j] < val:
                best = max(best, dist[i - 1][j])
        if i + 1 < n:
            if M[i + 1][j] < val:
                best = max(best, dist[i + 1][j])
        if j - 1 >= 0:
            if M[i][j - 1] < val:
                best = max(best, dist[i][j - 1])
        if j + 1 < m:
            if M[i][j + 1] < val:
                best = max(best, dist[i][j + 1])
        return best

    result = 0
    while Q.empty() == False:
        val, i, j = Q.get()
        dist[i][j] = mostoptimal(val, i, j) + 1
        if dist[i][j] > result:
            result = dist[i][j]

    return result

runtests(trip, all_tests=True)
input("Press Enter to exit...")