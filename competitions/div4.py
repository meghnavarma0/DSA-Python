

t = int(input())
while t:
    n, k = list(map(int, input().split()))
    result = []
    if k > n:
        print("NO")
    elif n % 2 != 0 and k % 2 == 0:
        print("NO")
    elif n % 2 == 0 and k % 2 != 0 and k > n//2:
        print("NO")

    elif n % 2 == 0:
        if k % 2 == 0:
            for i in range(k-1):
                result.append(1)
                n -= 1
            result.append(n)
        else:
            for i in range(k-1):
                result.append(2)
                n -= 2
            result.append(n)
    elif n % 2 != 0:
        for i in range(k-1):
            result.append(1)
            n -= 1
        result.append(n)
    print("YES")
    f = 0
    for i in result:
        print(i, end=" ")
        f = 1
    if f == 1:
        print()

    t -= 1
