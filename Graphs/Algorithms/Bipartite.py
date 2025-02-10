Graf=[[1],[0,2,4],[1,3,5],[2,4],[1,3],[2,6],[5,7],[6]]
from queue import Queue
def spojny(G):
    Q=Queue()
    n=len(G)
    visited=[False for _ in range(n)]
    visited[0]=True
    Q.put(0)
    while Q.empty()==False:
        u=Q.get()
        for i in G[u]:
            if visited[i]==False:
                visited[i]=True
                Q.put(i)
    for i in visited:
        if i==False:
            return False
    return True
def dwudzielny(G):
    if spojny(G)==False:
        return False
    n=len(G)
    kolory=[0 for _ in range(n)]
    def DFS(u):
        for v in G[u]:
            if kolory[v]==0:
                kolory[v]=-1*kolory[u]
                if DFS(v)==False:
                    return False
            elif kolory[v]==kolory[u]:
                return False
        return True
    kolory[0]=1
    return DFS(0)
