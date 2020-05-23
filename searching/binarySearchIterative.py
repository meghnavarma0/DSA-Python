def binSearch(arr, x):
    l = 0
    h = len(arr) - 1
    while l <= h:
        mid = (l + h)//2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return -1

arr = [1, 3, 5, 6, 9, 14, 78, 99]
print(binSearch(arr, 14))
