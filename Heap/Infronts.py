from heapq import heappush, heapify, heappop
def solve(heights, infronts):
    n = len(heights)
    heap = []
    for i in range(n):
        heappush(heap, (heights[i], infronts[i]))
    arr = [-1 for i in range(n)]
    while heap:
        element, pos = heappop(heap)
       
        c = 0
        for i in range(n):
            if c == pos and arr[i] == -1:
                arr[i] = element
                break

            if arr[i] == -1:
                c += 1
    return arr

heights = [5, 3, 2, 6, 1, 4]
infronts = [0, 1, 2, 0, 3, 2]
print(solve(heights, infronts))
        

    

