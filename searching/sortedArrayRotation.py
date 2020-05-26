# Write a program to find how many times is a sorted array rotated
def noOfRotation(arr):
    n = len(arr)
    low, high = 0, len(arr) - 1
    while low  <= high:
        if arr[low] <= arr[high]:
            return low
        mid = (low + high)//2
        prev = (mid - 1 + n)%n
        nxt = (mid + 1)%n
        if arr[mid] <= arr[prev] and arr[mid] <= arr[nxt]:
            return mid
        elif arr[mid] >= arr[low]:
            low = mid + 1
        elif arr[mid] <= arr[high]:
            high = mid - 1
    return -1

arr = [5, 6, 7, 8, 9, 1, 2, 3, 4]
print(noOfRotation(arr))
