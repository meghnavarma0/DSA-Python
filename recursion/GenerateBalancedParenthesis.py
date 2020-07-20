# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        
        def solve(op, c, o, result):
            if c == 0 and o == 0:
                result.append(op)
                return
            if o != 0:
                op1 = op + "("
                solve(op1, c, o-1, result)
            if o < c:
                op2 = op + ")"
                solve(op2, c-1, o, result)
        solve("", n, n, result)
        return result

        
        