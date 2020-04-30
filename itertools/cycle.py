# Demonstration of itertools cycle method

from itertools import cycle
s = "abc"
count = 0
a = cycle(s)
for i in a:
    if count == 10:
        break
    else:
        print(i, end=" ")
        count += 1
print()
print(list(a))
