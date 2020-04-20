from collections import Counter

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    d = Counter(arr)
    l = len(set(arr))
    f = 0
    for i in d:
        if d[i] > f:
            f = d[i]
    if f > l:
        print(l)
    elif f == l:
        print(l - 1)
    else:
        print(f)

    t -= 1
