# Given an array, find the maxium position where the sum of array elements ca exist.
# any two elements depicted by a, b can contain sum if 2a >= b, where a < b
# arr =  1 3 4
#       -1 4 4
#       -1 8 -1  -- 1
#       -1 -1 8  -- 2
# return 2

def check(arr, n):
    arr.sort()
    brr = []
    s = 0
    for i in arr:
        s += i
        brr.append(s)
    i = n - 1
    j = n - 2
    result = 1
    while brr[j] * 2 >= arr[i]:
        result += 1
        j -= 1
        i -= 1
        if j < 0:
            break
    return result

t = int(input())

while t:
    
    n = int(input())
    arr = list(map(int, input().split()))
    print(check(arr, n))
    
    t -= 1

