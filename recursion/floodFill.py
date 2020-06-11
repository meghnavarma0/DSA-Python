# Given a matrix with numbers denoting a specific color, return a matrix with color changed in adjacent cells with same color
# a = [[0, 0, 0, 3, 3, 3 ,4],
#      [0, 5, 3, 3, 3, 2, 2],
#      [0, 5, 3, 3, 5, 7, 3],
#      [0, 5, 2, 3, 5, 3, 3],
#      [0, 5, 2, 3, 5, 3, 3]]  
#  
a = [[0, 0, 0, 3, 3, 3 ,4],
     [0, 5, 3, 3, 3, 2, 2],
     [0, 5, 3, 3, 5, 7, 3],
     [0, 5, 2, 3, 5, 3, 3],
     [0, 5, 2, 3, 5, 3, 3]]

totalRows = len(a)
totalColumns = len(a[0])

def printMatrix(a):
    # global totalColumns
    # global totalRows

    for i in range(totalRows):
        for j in range(totalColumns):
            print(a[i][j], end=' ')
        print()

def floodFill(a, r, c, fromColor, toColor):

    # global totalColumns
    # global totalRows

    if r < 0 or r >= totalRows or c < 0 or c >= totalColumns:
        return
    
    if a[r][c] != fromColor:
        return

    a[r][c] = toColor
    floodFill(a, r - 1, c, fromColor, toColor)
    floodFill(a, r + 1, c, fromColor, toColor)
    floodFill(a, r, c - 1, fromColor, toColor)
    floodFill(a, r, c + 1, fromColor, toColor)

floodFill(a, 0, 0, 0, 8)
printMatrix(a)

 

    