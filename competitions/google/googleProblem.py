# There are N words in a dictionary such that each word is of fixed length and M consists only of lowercase English letters, that is ('a', 'b', ...,'z')
# A query word is denoted by Q. The length of query word is M. These words contain lowercase English letters but at some places instead of a letter between 'a', 'b', ...,'z' there is '?'. Refer to the Sample input section to understand this case.

# A match count of Q, denoted by match_count(Q) is the count of words that are in the dictionary and contain the same English letters(excluding a letter that can be in the position of ?) in the same position as the letters are there in the query word Q. In other words, a word in the dictionary can contain any letters at the position of '?' but the remaining alphabets must match with the query word.


# You are given a query word Q and you are required to compute match_count.


# Input Format

# The first line contains two space-separated integers N and M denoting the number of words in the dictionary and length of each word respectively.
# The next N lines contain one word each from the dictionary.
# The next line contains an integer Q denoting the number of query words for which you have to compute match_count.
# The next Q lines contain one query word each.

# Output Format
# For each query word, print match_count for a specific word in a new line.

# Constraints

# 1 <= N <= 5X10^4
# 1 <= M <= 7 
# 1 <= Q <= 10^5

# INPUT                # OUTPUT

# 5 3                  ['cat', 'map', 'bat', 'man', 'pen']
#                      ['?at', 'ma?', '?a?', '??n']
# cat                  2
# map                  2
# bat                  4
# man                  2          
# pen   
# 4
# ?at
# ma?
# ?a?
# ??n

# computes and returns true for matched pattern
def solve(string1, string2, m, n):
    if m != n:
        return False
    t = [[0 for i in range(n+1)] for j in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1] or string2[j-1] == "?":
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[m][n] == m


n, m = list(map(int, input().split()))
arr = []
pattern = []
for i in range(n):
    arr.append(input())
t = int(input())
for i in range(t):
    pattern.append(input())

print(arr)
print(pattern)
for i in pattern:
    c = 0
    for j in arr:
        if solve(j, i, len(j), len(i)):
            c += 1
    print(c)

