m, n = map(int, input().split())
array = list(map(int, input().split()))

def dduck(array, target,m):
    start = 0
    end = max(array)
    result = 0

    while start <= end:
        total =0
        mid = (start + end) // 2
        for i in array:
            if i > mid:
                total=total+i-mid
        if total < target:
            end = mid-1
        else:
            result = mid
            start = mid + 1
    return result




result = dduck(array,n,m)
print(result)


"""
4 6
19 15 10 17
"""