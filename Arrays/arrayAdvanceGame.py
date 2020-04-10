# Given that the element of an array depicts the total number of steps one can advance. Find out whether it is possible to reach the end(last index) of the array.
# eg if arr = [2, 0, 1, 3, 0, 0, 0] => YES
# if arr = [3, 2, 1, 0, 0, 5] => NO


def array_advance(arr):
    farthest_reched = 0
    for i in range(len(arr)):
        if i > farthest_reched:
            print("NO")
            return
        farthest_reched = max(farthest_reched, arr[i] + i)
    print("Yes")


t = int(input())
while t:
    arr = list(map(int, input().split()))
    array_advance(arr)
    t -= 1
