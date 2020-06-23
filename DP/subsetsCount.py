# Given an array, A, and a number, num. Finde the number of subsets of A that add up to num.

def count(A, num):
    n = len(A)
    t = [[0 for i in range(num + 1)] for j in range(n + 1)]
    for j in range(num + 1):
        t[0][j] = 0
    for i in range(n + 1):
        t[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, num + 1):
            if A[i - 1] <= j:
                t[i][j] = t[i-1][j - A[i - 1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    print(t)
    return t[n][num]

arr = [2, 3, 5, 6, 8, 10]
num = 10
print(count(arr, num))
        