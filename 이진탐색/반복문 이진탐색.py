array = list(map(int, input().split()))
target = int(input())
end = len(array)
start = 0

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        print("start:",start,"mid:", mid, "end:",end)
        if array[mid] == target:
            return mid+1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

result = binary_search(array, target, start, end)

if result == None:
    print("정답 없음")
else:
    print(result)

