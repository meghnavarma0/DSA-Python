# You are given K eggs, and you have access to a building with N floors from 1 to N. 

# Each egg is identical in function, and if an egg breaks, you cannot drop it again.

# You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

# Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

# Your goal is to know with certainty what the value of F is.

# What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

 

# Example 1:

# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
# Example 2:

# Input: K = 2, N = 6
# Output: 3
# Example 3:

# Input: K = 3, N = 14
# Output: 4


class Solution:
    def __init__(self):
        self.t = [[-1 for i in range(10001)] for j in range(101)]
    def superEggDrop(self, e: int, f: int) -> int:
        if f == 0 or f == 1 or e == 1:
            return f
        if self.t[e][f] != -1:
            return self.t[e][f]
        ans = sys.maxsize
        
        
        for k in range(1, f+1):
            
            if self.t[e-1][k-1] != -1:
                a = self.t[e-1][k-1]
            else:
                a = self.superEggDrop(e-1, f-1)
                self.t[e-1][k-1] = a
            
            if self.t[e][f-k] != -1:
                b = self.t[e][f-k]
            else:
                b = self.superEggDrop(e, f-k)
                self.t[e][f-k] = b
            temp = 1 + max(a, b)
            ans = min(ans, temp)
        return ans
            
            
        