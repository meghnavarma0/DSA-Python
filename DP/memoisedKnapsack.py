mem = [[-1 for i in range(10 + 1)] for j in range(4 + 1)]

def knapsack(val, wt, w, n):
    
    if w == 0 or n == 0:
        return 0
    if mem[n][w] != -1:
        return mem[n][w]
    if wt[n-1] <= w:
        result = max(val[n-1] + knapsack(val, wt, w - wt[n-1], n-1), knapsack(val, wt, w, n-1))
    elif wt[n-1] > w:
        result = knapsack(val, wt, w, n-1)
    mem[n][w] = result
    return result

val = [2, 4, 5, 7]
wt = [3, 5, 7, 1]

print(knapsack(val, wt, 10, len(val)))