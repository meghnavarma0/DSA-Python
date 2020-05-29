from heapq import heappush, heappop
# Print k largest elements in an array

def findLargest(arr, k):
    b = []
    for i in arr:
        heappush(b, i)
        if len(b) > k:
            heappop(b)
    return b

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(findLargest(arr, k))

