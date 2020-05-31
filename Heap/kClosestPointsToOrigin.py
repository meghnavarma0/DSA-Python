# Given an array of coordinates, find the k closest points to origin
from heapq import heappush, heappop
def kClosest(arr, k):
    result = []
    heap = []
    for i in arr:
        key = i[0]**2 + i[1]**2
        heappush(heap, [-1 * key, i])
        if len(heap) > k:
            heappop(heap)
    while heap:
        result.append(heappop(heap)[1])
    return result

arr = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
res = kClosest(arr, k)
for i in res:
    print(i)

    
    