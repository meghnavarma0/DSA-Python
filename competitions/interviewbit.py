
def solve(A):
    
    def lcs(a, b):
        m, n = len(a), len(b)
        t = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i-1] == b[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        s = ""
        i, j = m, n
        while i > 0 and j > 0:
            if a[i-1] == b[j-1]:
                s = a[i-1] + s
                i -= 1
                j -= 1
            elif t[i-1][j] > t[i][j-1]:
                s = a[i-1] + s
                i -= 1
            else:
                s = b[j-1] + s
                j -= 1
        while i > 0:
            s = a[i-1] + s
            i -= 1
        while j > 0:
            s = b[j-1] + s
            j -= 1
        return s
    l = len(A)         
    if l == 1:
        return len(A[0])
        
    
    while len(A) > 1:
        a = A.pop()
        b = A.pop()
        c = lcs(a, b)
        print("c is", c)
        A.append(c)
        print(A)
        
        
    return len(A[0])
        

A =  [ "bcd", "ab", "cd" ]
print(solve(A))
    
        
        
