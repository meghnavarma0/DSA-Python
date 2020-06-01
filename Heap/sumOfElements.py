# Find the sum of elements of array between k1th smallest and k2th smallest element.
from heapq import heappush, heappop
def kthSmallest(arr, k):
    heap = []
    for i in arr:
        heappush(heap, -1 * i)
        if len(heap) > k:
            heappop(heap)
    return -1*heappop(heap)

arr = [1, 3, 6, 2, 12, 9]
k1 = 3
k2 = 6
res = 0
a = kthSmallest(arr, k1)
b = kthSmallest(arr, k2)
print(a, b)
if a > b:
    a, b = b, a
for i in arr:
    if i > a and i < b:
        res += i
print(res)