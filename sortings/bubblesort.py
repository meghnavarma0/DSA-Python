# Program to implement assending order bubble sort


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [8, 7, 6, 5, 4, 3, 2, 1]
bubblesort(arr)
print(arr)
