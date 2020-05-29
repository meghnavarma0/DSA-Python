# Find kth smallest element in the given array 
import heapq

def findElement(arr, k):
    brr = []
    heapq.heapify(brr)
    for i in arr:
        heapq.heappush(brr, -1 * i)
        if len(brr) > k:
            heapq.heappop(brr)

    return(-1 * brr[0])


arr = [7, 10, 4, 3, 20, 15]

k = 3

print(findElement(arr, k))


