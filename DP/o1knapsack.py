def knapsack(val, wt, w, n):

    if w == 0 or n == 0:
        return 0
    if wt[n-1] <= w:
        return max(val[n-1] + knapsack(val, wt, w - wt[n-1], n-1), knapsack(val, wt, w, n-1))
    elif wt[n-1] > w:
        return knapsack(val, wt, w, n-1)

val = [2, 4, 5, 7]
wt = [3, 5, 7, 1]

print(knapsack(val, wt, 10, len(val)))