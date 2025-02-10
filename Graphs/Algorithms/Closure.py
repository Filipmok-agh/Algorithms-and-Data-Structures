def clausure(G):
    n=len(G)
    for i in range(n):
        for u in range(n):
            for w in range(n):
                if G[u][w]==True:
                    pass
                else:
                    if G[u][i] and G[i][w]:
                        G[u][w]=True
    return G