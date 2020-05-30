# Given an array, sort elements in decreasing order of frequency
# eg. arr = [1, 1, 2, 4, 3, 3, 3, 4, 4, 4] --> [4, 4, 4, 4, 3, 3, 3, 1, 1, 2]
# [4, 4, 4, 4, 3, 3, 3, 1, 1, 2] --> expected result
# [4, 4, 4, 4, 3, 3, 3, 1, 1, 2] --> my output
from collections import Counter
from heapq import heappop, heappush
def frequencySort(arr):
    result = []
    d = Counter(arr)
    heap = []
    for i in d:
        heappush(heap, (-1 * d[i], i))
    while heap:
        a = heappop(heap)
        for i in range(d[a[1]]):
            result.append(a[1])
    return result

arr = [1, 1, 2, 4, 3, 3, 3, 4, 4, 4]
print(frequencySort(arr))
    

