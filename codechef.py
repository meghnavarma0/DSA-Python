def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)


def isCoprime(a, b):

    if gcd(a, b) == 1:
        return True
    return False


def pack(arr):

    result = [arr[0]]

    if (len(arr) > 1):

        for i in range(1, len(arr)):
            f = True
            for j in result:
                if isCoprime(arr[i], j) == False:

                    f = False
                    break
            if f:
                result.append(arr[i])

    return (len(result), result)


t = int(input())
while t:
    n = int(input())
    arr = [i for i in range(1, n + 1)]

    print(n//2)
    for i in range(n//2):
        num, result = pack(arr)
        print(num, end=" ")
        for j in result:
            print(j, end=" ")
        print()

        next = []
        for j in arr:
            if j not in result:
                next.append(j)
        arr = next
    t -= 1
