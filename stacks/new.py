def findMin(s):

    result = int(s[0])
    ans = ""
    k = 0
    while(k < result):
        ans += "("
        k += 1
    ans += s[0]
    for i in range(1, len(s)):
        a = int(s[i - 1])
        b = int(s[i])
        if a < b:
            result = b - a
            k = 0
            while(k < result):
                ans += "("
                k += 1

        elif a > b:
            result = a - b
            k = 0
            while(k < result):
                ans += ")"
                k += 1

        ans += s[i]
    k = 0
    result = int(s[-1])
    while(k < result):
        ans += ")"
        k += 1

    return ans


t = int(input())

p = 1

while(p <= t):

    s = input()

    result = findMin(s)

    print("Case #{}: {}".format(p, result))

    p += 1
