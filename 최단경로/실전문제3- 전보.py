import sys
import heapq
input = sys.stdin.readline
n,m,c = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(start, 0))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+ i[1]
            if distance[i[0]]> cost:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))




dijkstra(c)

count =0
time = 0
for i in distance:
    if i != INF:
        count+=1
        time = max(i, time)
print(count-1, time)