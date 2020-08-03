# Not a working solution

n = 8
def printMatrix(arr, n):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()

def isSafe(arr, x, y):
    if x >= 0 and x < n and y >= 0 and y < n and arr[x][y] == -1:
        return True
    return False

def solve(arr, pos, n, curr_x, curr_y, move_x, move_y):
    
    if pos == n**2:
        return True
    for i in range(n):
        next_x = curr_x + move_x[i]
        next_y = curr_y + move_y[i]
        if isSafe(arr, next_x, next_y):
            arr[next_x][next_y] = pos 
            if solve(arr, pos+1, n, next_x, next_y, move_x, move_y):
                return True
                break
            arr[next_x][next_y] = -1
    return False

if __name__ == "__main__":
    n = 8
    move_x = [-2, -2, -1, 1, 2, 2, 1, -1]
    move_y = [1, -1, -2, -2, -1, 1, 2, 2]
    arr = [[-1 for i in range(n)] for j in range(n)]
    arr[0][0] = 0
    pos = 1
    if not solve(arr, pos, n, 0, 0, move_x, move_y):
        print("Solution does not exist")
    else:
        printMatrix(arr, n)