# given a two dimesional array( arr[m][n] ) sorted row and column wise. Search a key O(n + m) time complexty.

def search(arr, m, n, key):
    i = 0
    j = n - 1


    while i >= 0 and i < m and j >= 0 and j < n:
        if arr[i][j] == key:
            ans = (i, j)
            return ans
        if key < arr[i][j]:
            j -= 1
        else:
            i += 1
    return (-1)

t = int(input())
while t:
    arr = []
    m, n, key = list(map(int, input().split()))
    for i in range(m):
        brr = list(map(int, input().split()))
        arr.append(brr)
    print(search(arr, m, n, key))
    t -= 1
