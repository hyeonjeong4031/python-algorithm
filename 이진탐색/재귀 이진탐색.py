target= int(input())
array = list(map(int, input().split()))
end = len(array)
start = 0

def binary_search(array, target, end, start):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid]> target:
        binary_search(array, target, mid-1, start)
    else:
        binary_search(array, target, end, mid+1)
    return None

result = binary_search(array, target, end, start)

if result == None:
    print("정답 없음")
else:
    print(result+1)

