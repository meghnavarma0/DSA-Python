

def squaredSubsequence(arr, n):
    count = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            if product % 4 == 0 or product % 2 != 0:
                count += 1
    return count


t = int(input())
while t:

    n = int(input())
    arr = list(map(int, input().split()))
    print(squaredSubsequence(arr, n))

    t -= 1
