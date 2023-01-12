store = list(map(int, input().split()))
customerReq = list(map(int, input().split()))

def binary_module(array, target, start, end):
    mid = (start+end)//2
    if start > end:
        return None
    if array[mid]==target:
        return True
    elif target > array[mid]:
        return binary_module(array,target,mid+1, end)
    else:
        return binary_module(array,target,start, mid-1)

def result(array):
    array.sort()
    start = 0
    end = len(array)-1
    for i in customerReq:
        target = i
        result = binary_module(array, target, start, end)
        if result==None:
            print("no", end=" ")
        else:
            print("yes", end=" ")

binary_Search = result(store)

