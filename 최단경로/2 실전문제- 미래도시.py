INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int, input().split())

for a in range(n+1):
    for b in range(n+1):
        if a == b :
            graph[a][b] = 0


# 1번 노드에서  k를 거쳐 x로 간다
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

distance = graph[1][k] + graph[k][x]


"""
4 2
1 3
2 4
3 4

"""