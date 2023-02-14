n = int(input())
nList = list(map(int, input().split()))
nList.sort()
count = 0
result = 0

for i in nList:
    count += 1
    if i <= count:
        count = 0
        result += 1


print(result)
"""
1
1 2 3 4 5
"""