n = 5
graph = [[]for i in range(n+1)]

# for _ in range(3):
#     a,b,c = map(int, input().split())
#     graph[a].append(b,c)
# print(graph)
#
for _ in range(3):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
print(graph)

"""
1 2 3
1 2 4
2 2 5
"""