def check(arr):

    # print(arr)
    result = ""
    alist = []
    blist = []

    for i in range(len(arr)):
        if arr[i][0] == "":
            blist.append(arr[i][1])
            # result += arr[i][1]
        elif arr[i][-1] == "":
            # result = arr[i][0] + result
            alist.append(arr[i][0])
        else:
            a, b = arr[i]
            alist.append(a)
            blist.append(b)
    l = 0
    p = 0
    for i in range(len(alist)):
        k = len(alist[i])
        if k > l:
            l = k
            p = i
    result = alist[p]
    l = 0
    for i in range(len(blist)):
        k = len(blist[i])
        if k > l:
            l = k
            p = i
    result += blist[p]

    for i in blist:
        k = len(i)
        if result[-k:] != i:
            return "*"
    for i in alist:
        k = len(i)
        if result[: k] != i:
            return "*"

    return result


t = int(input())
p = 1
while p <= t:

    n = int(input())
    arr = []
    for i in range(n):
        s = input().strip().split("*")

        arr.append(s)
    result = check(arr)
    print("Case #" + str(p) + ":", result)

    p += 1
