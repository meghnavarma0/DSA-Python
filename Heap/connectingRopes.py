# given an array of rope length, cost signifies the sum of length of two ropes. Find the minimum cost of connecting all the ropes.
from heapq import heapify, heappop, heappush
def connectingRopes(arr):
    heapify(arr)
    print(arr)
    result = 0
    while (len(arr) > 1):
        a = heappop(arr)
        b = heappop(arr)
        t = a + b
        result += t
        heappush(arr, t)
    return result

arr = [5, 3, 2, 4, 1]
print(connectingRopes(arr))

