def binSearch(arr, l, h, x):
    if l <= h:
        mid = (l + h)//2
        if arr[mid] == x:
         
            return mid
        elif x < arr[mid]:
            return binSearch(arr, l, mid - 1, x)
        else:
            return binSearch(arr, mid + 1, h, x)
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binSearch(arr, 0, len(arr) - 1, 6))