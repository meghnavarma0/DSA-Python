t = int(input())
while t:
    n, k = list(map(int, input().split()))

    extra = k % (n-1)
    key = k // (n-1)
    if k % (n-1) == 0:
        key -= 1
        extra = n-1
    result = n * (key) + extra
    print(result)

    t -= 1
