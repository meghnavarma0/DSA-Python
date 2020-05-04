def partition(arr, l, r):

    pivot = arr[r]
    i = -1
    j = 0
    while j < r:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1
    arr[i], arr[j] = arr[j], arr[i]
    return i


def quicksort(arr, l, r):
    if(l < r):
        p = partition(arr, l, r)
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, r)


arr = [9, 52, 6, 8, 4, 8, 12, 24, 86, 89, 100, 286, 0]
quicksort(arr, 0, len(arr)-1)
print(arr)
