Find the length of longest common subsequence between two strings.
def lcs(x, y, m, n, mem):
    result = None

    if m == 0 or n == 0:
        return 0
    
    if mem[m][n] != -1:
        return mem[m][n]

    elif x[m-1] == y[n-1]:
        result = 1 + lcs(x, y, m-1, n-1, mem)
    
    else:
        result = max(lcs(x, y, m-1, n, mem), lcs(x, y, m, n-1, mem))
    
    mem[m][n] = result
    return result

x = "abdfght"
y = "abdkhkjh"
m = len(x)
n = len(y)
mem = [[-1 for i in range(n+1)] for j in range(m+1)]
print(lcs(x, y, m, n, mem))
    
    
