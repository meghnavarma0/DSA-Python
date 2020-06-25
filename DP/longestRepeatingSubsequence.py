def LRS(s):
    a = s[::]
    b = s[::]
    n = len(a)
    t = [[0 for i in range(n + 1)] for j in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1] and i != j:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    return t[n][n]

s = "AABEBCDD"
print(LRS(s))
