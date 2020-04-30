# Python program to demonstrate infinite iterators
from itertools import count
arr = []
for i in count(5, 5):
    if i == 35:
        break
    else:
        arr.append(i)

print(arr)
