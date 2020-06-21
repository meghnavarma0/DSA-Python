# A nearly sorted array is defined by an array where all elemnts that are supposed to be at index i in the sorted array can be found in the range if indices between i - 1 and i + 1, both inclusive. Return the index of the elemnt. If found, otherwise return -1.

def binarySearch(arr, n):
    start, end, mid = 0, len(arr) - 1, None
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == n:
            return mid
        elif mid - 1 >= start and arr[mid - 1] == n:
            return mid - 1
        elif mid + 1 <= end and arr[mid + 1] == n:
            return mid + 1
        elif n < arr[mid]:
            end = mid - 2
        else:
            start = mid + 2
    return -1

arr = [5, 10, 30, 20, 40]
print(binarySearch(arr, 30))
print(binarySearch(arr, 20))
print(binarySearch(arr, 40))
print(binarySearch(arr, 17))