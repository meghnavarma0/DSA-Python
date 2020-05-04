def maxDiv(a, b):
    while a % b == 0:
        a /= b
    return a


def isUgly(no):
    no = maxDiv(no, 2)
    no = maxDiv(no, 3)
    no = maxDiv(no, 5)

    return 1 if no == 1 else 0


def nthUgly(n):

    i = 1
    count = 1

    while count < n:
        i += 1
        if isUgly(i):
            count += 1

    return i


t = int(input())
while t:
    n = int(input())
    print(nthUgly(n))

    t -= 1
