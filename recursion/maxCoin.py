# You and your friend are playing a game of coins. A player can select a coin from either end of an array of coins. Each coin has a number written on it. Both the players choose alternatively in an optimal way. Find the maximum sum of all the numbers you can gain if you select the first coin. The coins are depicted by an array of numbers.

a = [1, 5, 700, 8]

def coinMax(a, l, r):
    if l+1 == r:
        return max(a[l], a[r])
    return max(a[l] + min(coinMax(a, l+2, r), coinMax(a, l+1, r-1)),
               a[r] + min(coinMax(a, l+1, r-1), coinMax(a, l, r-2)))

print(coinMax(a, 0, len(a)-1))
