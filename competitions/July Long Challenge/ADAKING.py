t = int(input())

while t:
    n = int(input())
    a = [["X" for i in range(8)] for j in range(8)]
    #a[0][0] = "O"
    for i in range(8):
        for j in range(8):
            if n:
                a[i][j] = "."
                n -= 1
            else:
                break
        if not n:
            break
    a[0][0] = "O"
    for i in range(8):
        print(" ".join(a[i]))
    print()
    t -= 1
