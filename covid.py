def maxProfit(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)):
        arr[i] -= i
        if arr[i] < 0:
            arr[i] = 0

    return(sum(arr) % (10**9 + 7))


t = int(input())
while t:

    n = int(input())
    arr = list(map(int, input().split()))
    print(maxProfit(arr))

    t -= 1
