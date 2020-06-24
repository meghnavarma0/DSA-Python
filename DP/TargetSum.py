# Given an array of numbers, arr, and a target sum, s. Find the number of ways in which the given arry sums up to s, if you are allowed to assign either + or - sign to each array element.


def targetSum(arr, s):
    n = len(arr)
    t = [[0 for i in range(s + 1)] for j in range(n + 1)]
    # Initialization
    for i in range(s + 1):
        t[0][i] = 0
    for i in range(n + 1):
        t[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, s + 1):

            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] + t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    print(t)
    return t[n][s]

arr = [1, 1, 2, 3]
s = 1
s1 = (sum(arr) + s)//2

print(targetSum(arr, s1))

    