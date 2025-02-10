Graf=[[1,2],[3],[4],[5],[1],[2]]
def TOPO(G):
    def DFSvisit(G,v):
        nonlocal lista
        nonlocal time
        visited[v]=True
        for i in G[v]:
            if visited[i]==False:
                DFSvisit(G,i)
        time+=1
        lista[n-time]=v
    n=len(G)
    lista=[None for _ in range(n)]
    time=0
    visited = [False for _ in range(n)]
    for v in range(n):
        if visited[v]==False:
            DFSvisit(G,v)
    return lista
def Topo(Graf):
    Graf=TOPO(Graf)
    return Graf
Cykl=Topo(Graf)
def Hamilton(G):
    Cykl = Topo(G)
    print(Cykl)
    print(G)
    for i in range(1,len(Cykl)):
        a=Cykl[i-1]
        b=Cykl[i]
        if b in G[a]:
            pass
        else:
            return False
    return True



