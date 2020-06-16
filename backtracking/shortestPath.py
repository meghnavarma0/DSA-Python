def isValid(arr, i, j, visited):
    m = len(arr)
    n = len(arr[0])
    if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or not arr[i][j]:
        return False
    return True

def shortestPath(arr, i, j, x, y):
    m = len(arr)
    n = len(arr[0])
    visited = [[False for i in range(n)] for j in range(m)]
    ans = shortestPath2(arr, i, j, x, y, visited)
    if ans >= 1000000:
        return "Not possible to reach"
    return ans





def shortestPath2(arr, i, j, x, y, visited):
    if not isValid(arr, i, j, visited):
        return 1000000
    if i == x and j == y :
        return 0
    visited[i][j] = True

    left = 1 + shortestPath2(arr, i, j-1, x, y, visited)
    top = 1 + shortestPath2(arr, i-1, j, x, y, visited)
    right = 1 + shortestPath2(arr, i, j+1, x, y, visited)
    bottom = 1 + shortestPath2(arr, i+1, j, x, y, visited)
    

    visited[i][j] = False

    return min(left, top, right, bottom)


arr = [[1, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 0],
       [1, 1, 1, 1, 0, 0, 0, 0, 0] 
                                    
                                    ]
print(shortestPath(arr, 0, 0, 7, 2))

