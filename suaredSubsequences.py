import math


def subs(n):
    val = math.ceil(math.sqrt(n))
    upper = val**2
    diff = upper - n
    return math.ceil(math.sqrt(diff)) == math.floor(math.sqrt(diff))


def squaredSubsequence(arr, n):
    count = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            if subs(product):
                count += 1
    return count


t = int(input())
while t:

    n = int(input())
    arr = list(map(int, input().split()))
    print(squaredSubsequence(arr, n))

    t -= 1
