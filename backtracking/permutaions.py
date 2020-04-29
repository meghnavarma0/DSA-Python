# Program to find all permutations of a given string.
def permute(arr, l, r):
    if l == r:
        print("".join(arr), end=" ")
        return
    for i in range(l, r + 1):
        arr[i], arr[l] = arr[l], arr[i]
        permute(arr, l + 1, r)
        arr[i], arr[l] = arr[l], arr[i]


n = int(input())
arr = input()
arr = list(arr)
permute(arr, 0, n - 1)
