# Return an array of top k most frequent numbers

from collections import Counter
from heapq import heappop, heappush

def kMostFrequents(arr, k):
    d = Counter(arr)
    result = []
    a = [(d[i], i) for i in d]
    heap = []
    for i in a:
        heappush(heap, i)
        if len(heap) > k:
            heappop(heap)
    
    while heap:
        result.append(heappop(heap)[1])
    return result



arr = [1, 1, 2, 1, 3, 2, 4, 1, 3, 3]
print(kMostFrequents(arr,2))