Graf=[[1,7],[2],[0,3],[6],[3,9],[4,8],[5],[8],[9],[7,10],[8]]
def silneskladowe(G):
    def DFSvisit(G,v):
        nonlocal time
        time += 1
        przejscie[v]=time
        visited[v]=True
        for i in G[v]:
            if visited[i]==False:
                DFSvisit(G,i)
        time+=1
        przetworzenie[v]=[time,v]
    n=len(G)
    time =0
    visited = [False for _ in range(n)]
    przejscie=[-1 for _ in range(n)]
    przetworzenie=[-1 for _ in range(n)]
    DFSvisit(G,0)
    def revers(G):
        n = len(G)
        T = [[] for _ in range(n)]
        for i in range(n):
            for j in G[i]:
                T[j].append(i)
        return T
    G=revers(G)
    kolejnosc = sorted(przetworzenie, reverse=True)
    visited = [False for _ in range(n)]
    res=[]
    def DFS(G, v,kol):
        visited[v] = True
        for i in G[v]:
            if visited[i] == False:
                res[kol].append(i)
                DFS(G, i,kol)
    cnt=0
    for i in range(n):
        if visited[kolejnosc[i][1]]==False:
            res.append([])
            res[cnt].append(kolejnosc[i][1])
            DFS(G,kolejnosc[i][1],cnt)
            cnt+=1
    print(res)
print(silneskladowe(Graf))