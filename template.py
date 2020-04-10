def maxProfit(arr):
    pass


t = int(input())
while t:

    n = int(input())
    arr = list(map(int, input().split()))
    print(maxProfit(arr))

    t -= 1