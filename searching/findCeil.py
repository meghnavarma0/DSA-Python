def findCeil(arr, x):

    low = 0
    high = len(arr) - 1
    mid = None
    result = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        
        elif x < arr[mid]:
            result = arr[mid]
            high = mid - 1

        else:
            low = mid + 1

    return result

arr = [1, 2, 3, 6, 9, 10, 20, 78]
print(findCeil(arr, 8))
print(findCeil(arr, 21))
print(findCeil(arr, 90))