from heapq import heappop, heappush
# sort a k sorted array. 
# A k sorted array is one which has the required element in the range ofkelements

def KSorted(arr, k):

    a = []
    j = 0
    for i in arr:
        heappush(a, i)
        if len(a) > k:
            arr[j] = heappop(a)
            j += 1
        
    while a:
        arr[j] = heappop(a)
        j += 1

arr = [6, 5, 3, 2, 8, 10, 9]
KSorted(arr, 3)
print(arr)

