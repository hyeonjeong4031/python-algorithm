size = int(input())
array = []

for i in range(size):
    array.append(list(map(int, input().split())))


for i in range(1, size):
    for j in range(0,i+1):
        if j == 0:
            array[i][0] += array[i-1][0]
        elif j == i:
            array[i][j] += array[i-1][j-1]
        else:
            array[i][j] += max(array[i-1][j-1], array[i-1][j])

print(max(array[size-1]))





"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""