# given an array and a number n, find k closest numbers from n

# eg. arr = [5, 6, 7, 8, 9], k = 3 , n = 7 --> [6, 7, 8]

from heapq import heappop, heappush

def kClosest(arr, k, n):
    a = []
    result = []
    b = [(-1 * abs(n - i), i) for i in arr]
    for i in b:
        heappush(a, i)
        if len(a) > k:
            heappop(a)
    while a:
        result.append(heappop(a)[1])
    return result


arr = [5, 6, 7, 8, 9]
k = 3 
n = 7
print(kClosest(arr, k, n))