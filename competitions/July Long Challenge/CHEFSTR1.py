t = int(input())
while t:

    result = 0
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        result += abs(arr[i] - arr[i-1]) - 1
    print(result)
        

    t -= 1
