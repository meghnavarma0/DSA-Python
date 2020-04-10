# Given an array of stocks, determine the maximum amount of profit one can possibly make by buying and selling in the same range.
# eg: arr = [350, 340, 290, 220, 230, 290, 210, 222] => 70 ie, buying @220 and selling at 290

# BRUTE FORCE:
# Time COmplexity: O(n^2)
# Space Complexity: O(1)


def buy_and_sell(arr):
    max_profit = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > max_profit:
                max_profit = arr[j] - arr[i]
    return max_profit


# Optimized Approach:
# Time Complexity: O(n)
# Space Complexity: O(1)

def buy_and_sell_optimal(arr):
    max_profit = 0
    current_difference = 0
    min_val = arr[0]
    for price in arr:
        if price < min_val:
            min_val = price
        current_difference = price - min_val
        max_profit = max(max_profit, current_difference)
    return max_profit


t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    print(buy_and_sell(arr))
    print(buy_and_sell_optimal(arr))
    t -= 1
