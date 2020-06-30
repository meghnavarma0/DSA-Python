import sys

def solve(arr, i, j):
    if i >= j:
        return 0
   
    mn = sys.maxsize
    for k in range(i, j):
        temp_ans = solve(arr, i, k) + solve(arr, k + 1, j) + arr[i-1] * arr[k] * arr[j]
       
        mn = min(mn, temp_ans)

    return mn

arr = [1, 2, 3, 4, 3]
print(solve(arr, 1, len(arr) - 1))

    