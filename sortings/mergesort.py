

def mergesort(arr):
    l = 0
    r = len(arr)

    if len(arr) > 1:
        q = len(arr)//2
        L = arr[:q]
        R = arr[q:]
        mergesort(L)
        mergesort(R)

        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


arr = [9, 7, 0, 3, 5, 6]
mergesort(arr)
print(arr)
