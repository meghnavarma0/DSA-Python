import math

def isPrime(n):
    m = int(math.sqrt(n))
    for i in range(2, m):
        if n % i == 0:
            return False
    return True


def strangeNum(f, p):
    if p == 1:
        if f == 2:
            return 1
        return 0
    else:
        if isPrime(f):
            return 1
        return 0


t = int(input())
while t:

    f, p = list(map(int, input().split()))
    print(strangeNum(f, p))

    t -= 1
