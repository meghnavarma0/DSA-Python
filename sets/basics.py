a = {1, 2, 3}
b = {2, 3, 4, 5, 6}

c = a.union(b)

print(c)

c2 = a | b
print(c2)

d = a.intersection(b)
print(d)

d2 = a & b
print(d2)

print("b > a : ", b > a)
print("a < c: ", a < c)  # a is a proper subset of c
