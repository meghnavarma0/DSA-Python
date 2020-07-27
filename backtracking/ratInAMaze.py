# In a boolean matrix, you have to reach from the first to the last block by moving along 1's.If possible, print the solution matrix, else print "NOT POSSIBLE"






def printMatrix(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()

def isSafe(x, y, maze):
    if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1:
        return True
    return False

def solve(x, y, arr, maze):
    if x == n-1 and y == n-1 and maze[x][y] == 1:
        printMatrix(arr)
        return True

    if isSafe(x, y, maze):
        arr[x][y] = 1
        if solve(x+1, y, arr, maze):
            return True
    
        if solve(x, y+1, arr, maze):
            return True
        arr[x][y] = 0
    
    return False



if __name__ == "__main__":
    n = 4
    maze = [ [1, 0, 0, 0], 
            [1, 1, 0, 1], 
            [0, 1, 0, 0], 
            [1, 1, 1, 1] ] 
    arr = [[0 for i in range(n)] for j in range(n)]
    if not solve(0, 0, arr, maze):
        print("NOT POSSIBLE")

