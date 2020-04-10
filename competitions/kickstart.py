t = int(input())
p = 1
while p <= t:
    n, b = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0
    i = 0
    while b >= arr[i] and i < n:
        b -= arr[i]
        i += 1
        count += 1
    print("Case #" + str(p) + ": " + str(count))

    p += 1
