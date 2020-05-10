def check(n):
    result = []

    while n > 0:
        s = str(n)
        l = len(s)-1
        result.append(pow(10, l) * int(s[0]))
        n %= result[-1]
    return result


t = int(input())
while t:

    n = int(input())
    result = check(n)
    print(len(result))
    for i in result:
        print(i, end=" ")

    t -= 1
