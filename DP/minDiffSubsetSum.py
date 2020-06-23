# Given an array, find the minimum difference that can be present between their sums on dividing the array into two sub-sets.
def check(arr):
    n = len(arr)
    s = sum(arr)
    v = []
    t = [[False for i in range(s + 1)] for j in range(n + 1)]
    for i in range(s + 1):
        t[0][i] = False
    for i in range(n + 1):
        t[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, s + 1):
            if arr[i - 1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i - 1][j]
            else:
                t[i][j] = t[i-1][j]
    for i in range(s//2 + 1):
        v = i
    
    return s - 2 * v

arr = [1, 6, 11, 5]
print(check(arr))
