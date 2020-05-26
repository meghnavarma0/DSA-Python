# given a sorted array, find the number of occurance of a given value in an array

def occurance(arr, x, first):
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == x:
            result = mid
            if first:
                high = mid - 1
            else:
                low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return result
arr = [1, 1, 2, 2, 2, 2, 4, 5, 7, 8]
firstIndex = occurance(arr, 2, True)
lastIndex = occurance(arr, 2, False)
print(firstIndex)
print(lastIndex)
print(lastIndex - firstIndex + 1)