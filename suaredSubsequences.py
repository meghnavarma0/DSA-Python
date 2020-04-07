import math


def subs(n):
    if n % 4 == 0 or n % 2 == 1:
        return True
    return False


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
