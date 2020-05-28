# Bitonic array is an array in which elements accur first in strictly increasing order and then strictly decreasing order.

def findPeak(arr):
    n = len(arr)

    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid + 1] > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        elif mid == 0:
            if arr[0] > arr[1]:
                return 0
            else:
                return 1
        elif mid == n - 1:
            if arr[n - 1] > arr[n - 2]:
                return n - 1
            else:
                return n - 2

def binarySearch(arr, x, low, high):
    # low = 0
    # high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def findBitonic(arr, x):
    n = len(arr)
    p = findPeak(arr)
    a = binarySearch(arr, x, 0, p)
    b = binarySearch(arr, x, p, n-1)
    if(a != -1):
        print(a)
    elif b != -1:
        print(b)
    else:
        print("ELEMENT NOT FOUND")

arr = [1, 2, 5, 9, 7, 4]
findBitonic(arr,10)
findBitonic(arr,1)
findBitonic(arr,9)