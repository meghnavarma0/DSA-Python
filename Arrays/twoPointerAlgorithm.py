# Given an array of integers. Find whether a combination of any two numbers sum up to a given target.
# eg arr = [-2, 1, 3, 5, 6], target = 4 => True


def twoSum(arr, target):
    arr.sort()
    i = 0
    j = len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return True
        if s < target:
            i += 1
        else:
            j -= 1
    return False


def twoSumUsingDict(arr, target):
    ht = {}
    for i in range(len(arr)):
        if arr[i] in ht:
            return True
        else:
            ht[target - arr[i]] = arr[i]
    return False


t = int(input())
while t:
    arr = list(map(int, input().split()))
    target = int(input())
    print(twoSum(arr, target))
    print(twoSumUsingDict(arr, target))
    t -= 1
