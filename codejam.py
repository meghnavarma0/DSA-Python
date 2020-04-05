def find(arr, n):

    testArray = sorted(arr)

    jobs_of_J = [testArray[0]]

    k = 0
    jobs_left = []
    jobs_of_C = []

    for i in range(1, n):
        if(testArray[i][0] >= jobs_of_J[-1][1]):
            jobs_of_J.append(testArray[i])
            k += 1
        else:
            jobs_left.append(testArray[i])

    if len(jobs_left) > 0:
        jobs_of_C = [jobs_left[0]]
        k = 0
        for i in range(1, len(jobs_left)):
            if(jobs_left[i][0] >= jobs_of_C[k][1]):
                jobs_of_C.append(jobs_left[i])
                k += 1
            else:
                return "IMPOSSIBLE"

    result = ["" for i in range(n)]
    for i in jobs_of_J:
        result[i[2]] = "J"
    if len(jobs_left) > 0:
        for i in jobs_of_C:
            result[i[2]] = "C"

    answer = ""

    for i in result:

        answer += i

    return answer


t = int(input())
p = 1
while(t):
    n = int(input())
    arr = []
    r = 0
    while r < n:

        limit = list(map(int, input().split()))
        limit.append(r)
        arr.append(limit)
        r += 1

    print("Case #{}: {}".format(p, find(arr, n)))

    t -= 1
    p += 1
