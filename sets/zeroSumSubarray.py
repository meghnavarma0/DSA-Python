# Given an array. Find whether there exsits a subarray with sum equal to 0. Given that len(arr) <= 10^5
def check(arr):
    p = set()
    totalSum = 0
    for i in range(len(arr)):
        totalSum += arr[i]
        if totalSum in p:
            return True
        else:
            p.add(totalSum)
    return False

t = int(input())
while t:

    arr = list(map(int, input().split()))
    print(check(arr))
    t -= 1


