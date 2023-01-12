import sys
storage = int(input())
foodCount = list(map(int, sys.stdin.readline().split()))

cashe = [0] * (storage+1)
#  인접하지 않은 리스트의 합이 최댓값
cashe[0] = foodCount[0]
cashe[1] = max(cashe[0], foodCount[1])

for i in range(2, storage):
    cashe[i] = max(cashe[i-1], (cashe[i-2]+foodCount[i]))



print(cashe[storage-1])
"""
4
1 3 1 5
"""