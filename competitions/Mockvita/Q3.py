import math
from collections import Counter, defaultdict
t = int(input())
arr = []
d2 = defaultdict(lambda: 0)
while t: 
    x, y, v = list(map(int, input().split()))
    val = math.sqrt(x*x + y*y)/v
    arr.append(val)
    d2[val] += 1


    t -= 1
# d = Counter(arr)

ans = 0
for i in d2.values():
    if i >= 2:
        ans += (i * (i - 1))//2
print(ans)

