from zad7testy import runtests
from math import inf

# Solution for traversing each column and selecting the optimal value based on movement direction
# Time complexity is: O(n^2)

def maze(maze_grid):
   def get_max_value(x, y):
      return max(distances[x][y][0], distances[x][y][1])

   size = len(maze_grid)
   distances = [[[-float('inf') for _ in range(2)] for _ in range(size)] for _ in range(size)]
   
   for i in range(size):
      for j in range(size):
         if maze_grid[i][j] == "#":
            distances[i][j][0] = -2
            distances[i][j][1] = -2

   for column in range(size):
      if column != 0:
         for row in range(size):
            if distances[row][column][0] != -2:
               if row == 0 and distances[row][column - 1][0] != -2:
                  distances[row][column][0] = get_max_value(row, column - 1) + 1
               if row != 0:
                  if distances[row][column - 1][0] != -2 and distances[row - 1][column][0] != -2:
                     distances[row][column][0] = max(get_max_value(row, column - 1), distances[row - 1][column][0]) + 1
                  elif distances[row][column - 1][0] != -2:
                     distances[row][column][0] = get_max_value(row, column - 1) + 1
                  elif distances[row - 1][column][0] != -2:
                     distances[row][column][0] = distances[row - 1][column][0] + 1

         for row in range(size - 1, -1, -1):
            if distances[row][column][0] != -2:
               if row == size - 1 and distances[row][column - 1][0] != -2:
                  distances[row][column][1] = get_max_value(row, column - 1) + 1
               if row != size - 1:
                  if distances[row + 1][column][0] != -2 and distances[row][column - 1][0] != -2:
                     distances[row][column][1] = max(get_max_value(row, column - 1), distances[row + 1][column][1]) + 1
                  elif distances[row][column - 1][0] != -2:
                     distances[row][column][1] = get_max_value(row, column - 1) + 1
                  elif distances[row + 1][column][0] != -2:
                     distances[row][column][1] = distances[row + 1][column][1] + 1
      else:
         for row in range(size):
            if distances[row][column][0] == -2:
               break
            distances[row][column][0] = row

   result = max(distances[size - 1][size - 1][0], distances[size - 1][size - 1][1])

   if result == -inf:
       result = -1

   return result
runtests( maze, all_tests = True )
input("Press Enter to exit...")
