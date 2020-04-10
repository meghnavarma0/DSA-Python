t = int(input())
while(t):
    n = int(input())
    p = 1
    i = 1
    if(n == 1):
        print(1)
    else:
        print(n//2)
    while i < n//2:
        if(i == 1):
            print(3, p, p + 1, p + 2)
            p += 3
        else:
            print(2, p, p + 1)
            p += 2
        i += 1
    if(p == n-1):
        print(2, p, p + 1)
    else:
        print(1, p)

    t -= 1
