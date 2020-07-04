def check(n):
    a = str(n)
    b = list(map(int, list(a)))
    return sum(b)


t = int(input())
while t:

    n = int(input())
    c = 0
    m = 0
    while n:
        a, b = list(map(int, input().split()))
        if check(a) > check(b):
            c += 1
        elif check(a) < check(b):
            m += 1
        else:
            c += 1
            m += 1
            
        n -= 1
    if c > m:
        print(0, c)
    elif m > c:
        print(1, m)
    else:
        print(2, c)
        

    t -= 1
