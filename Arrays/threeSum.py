def threeSum(arr, target):
    arr.sort()
    i = 0
    for i in range(len(arr) - 2):
        if twoSum(arr, target - arr[i], i + 1):
            return True
    return False


def twoSum(arr, target, i):

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


t = int(input())
while t:
    arr = list(map(int, input().split()))
    target = int(input())
    print(threeSum(arr, target))
    t -= 1
