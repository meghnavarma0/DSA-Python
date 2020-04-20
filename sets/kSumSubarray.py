# Given an array. Find whether there exsits a subarray with sum equal to k. Given that len(arr) <= 10^5
def check(arr, k):
    p = {0}
    totalSum = 0
    for i in range(len(arr)):
        totalSum += arr[i]
        if totalSum - k in p:
            return True
        else:
            p.add(totalSum)
    return False


t = int(input())
while t:
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(check(arr, k))
    t -= 1
