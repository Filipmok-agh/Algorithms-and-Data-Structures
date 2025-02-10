# My program identifies candidates from list P to be dominators.
# Each candidate is in the array T, and then I count how many elements it dominates.
# I then compare the count with the current leader in the dominator ranking.
# O(n^2)
from zad3testy import runtests

def dominance(P):
  def dominates(guy, a):
    if T[guy][0] > P[a][0] and T[guy][1] > P[a][1]:
      return True
    else:
      return False

  def domination_status(guy, a):
    if T[guy][0] > P[a][0] and T[guy][1] > P[a][1]:
      return 1
    if T[guy][0] < P[a][0] and T[guy][1] < P[a][1]:
      return 2
    else:
      return 0

  def inside(guy, a):
    if T[guy][0] > T[a][0] and T[guy][1] > T[a][1]:
      return 1
    if T[guy][0] < T[a][0] and T[guy][1] < T[a][1]:
      return 2
    else:
      return 0

  T = [P[0]]
  n = len(P)
  for i in range(1, n):
    flag = False
    l = len(T)
    for j in range(l):
      if domination_status(j, i) == 2:
        flag = True
        T[j] = P[i]
        cnt = 0
        k = j
        while k < l - cnt:
          if inside(j, k) == 1:
            cnt += 1
            T.pop(k)
          else:
            k += 1
        break
      elif domination_status(j, i) == 1:
        flag = True
        break
    if not flag:
      T.append(P[i])

  l = len(T)
  max_count = 0
  for i in range(l):
    count = 0
    for j in range(n):
      if dominates(i, j):
        count += 1
    if count > max_count:
      max_count = count

  return max_count

runtests(dominance, all_tests=True)
input("Press Enter to exit...")
