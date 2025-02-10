E=[[5, 0, 2], [0, 1, 3], [1, 2, 1], [5, 6, 1], [1, 6, 2], [5, 4, 6],
                  [4, 3, 8], [3, 6, 5], [2, 3, 7]]
class Node:
    def __init__(self,value):
        self.val=value
        self.parent=self
        self.rank=0
def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent
def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
def kruskal(G):
    Graf = [Node(i) for i in G]
    G.sort(key=lambda e: e[2])
    drzewo = []
    for k in G:
        u, v, waga = k
        if find(Graf[u])!=find(Graf[v]):
            union(Graf[u], Graf[v])
            drzewo.append(k)
    return drzewo
print(kruskal(E))