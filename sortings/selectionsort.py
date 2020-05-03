# Implement selection sort


def selectionsort(arr):
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range(i + 1, n):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]


arr = [5, 4, 3, 2, 1]
selectionsort(arr)
print(arr)
