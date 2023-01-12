
def binary(array, start, end, i):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == i:
            return 1
        elif array[mid] < i:
            start = mid+1
        else:
            end = mid - 1
    return 0

import sys
t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    answer = list(map(int, sys.stdin.readline().split()))
    array.sort()
    start = 0
    end = n - 1
    for i in answer:
        print(binary(array,start,end, i))

"""
5
4 1 5 2 3
5
1 3 7 9 5
"""