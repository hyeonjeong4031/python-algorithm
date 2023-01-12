import sys
input = sys.stdin.readline
import heapq
n,m = map(int, input().split())
# n = node의 수, m = 간선의 수
start = int(input())
graph = [[] for i in range(n+1)]
INF = int(1e9)
distance = [INF] * (n+1)


# 우선 distance를 입력받자!
for _ in range(m):
    a,b,c = map(int,input().split())
    #  a = 현제 노드 ,b= 이동할 노드, c = 간선의 길이
    graph[a].append((b,c))


# main 로직....
def dijkstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    #  큐가 빌때까지 반복
    while q:
        dist, node = heapq.heappop(q)
        # 큐에 있는 간선의 거리가 distance에 저장된 값보다 길면
        # 최솟값이 저장되있는것이 맞으므로 다음 큐로 이동한다.
        if distance[node] <dist:
            continue
        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start, distance,graph)

for i in range(1, n+1):
    if distance[i] == INF:
        print("inf")
    else:
        print(distance[i])

"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""