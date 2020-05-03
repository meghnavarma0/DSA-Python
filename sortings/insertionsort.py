def insertionsort(arr):

    n = len(arr)
    i = 1
    while(i < n):
        t = arr[i]
        j = i - 1
        while(j >= 0 and arr[j] > t):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = t
        i += 1


arr = [6, 9, 4, 3, 1, 8, 5]
insertionsort(arr)
print(arr)
