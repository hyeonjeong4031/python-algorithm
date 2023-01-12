import sys
# k, n = map(int, input().split())
# array = [int(sys.stdin.readline()) for _ in range(k)]
#
# start = 1
# end = max(array)
#
# while start <= end:
#     mid = (start + end)//2
#     count = 0
#     for i in array:
#         count += i//mid
#     if count >= n:
#         start = mid+1
#     else:
#         end = mid - 1
#
# print(end)

k = int(input())

def binary()

for _ in range(t):
    n = int(input())
    array1 = map(int, sys.stdin.readline().split())
    array1.sort()
    m = int(input())
    array2 = map(int, sys.stdin.readline().split())
    for i in array2:
        binary()







