import heapq
INF = int(1e9)
n,m= map(int, input().split())
#  간선 정보
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((c,b))
#  반드시 거쳐야 하는 두개의 서로 다른 정점, 사이에는 간선 최대 한개만 존재
u, v = map(int, input().split())

# 최단경로
distance = [INF] * (n+1)
def di ():
    q = []
    distance[1] = 0
    heapq.heappush(q,(1,0))
    while q:
        now,dist =  heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

di()






"""
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
"""