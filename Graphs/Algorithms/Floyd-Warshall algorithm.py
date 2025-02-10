Graf = [[[1,1]],[[2,3]],[[3,-7],[4,4]],[[0,1]],[]]
from math import inf
n=len(Graf)
T=[[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
    for indx,wart in Graf[i]:
        T[i][indx]=wart
def Floyd(G):
    n=len(G)
    S=G
    for k in range(n):
        for x in range(n):
            for y in range(n):
                if S[x][k] + S[k][y] < S[x][y]:
                    S[x][y] = S[x][k] + S[k][y]
    for k in range(n):
        for x in range(n):
            for y in range(n):
                if S[x][k] + S[k][y] < S[x][y]:
                    return False
    return S