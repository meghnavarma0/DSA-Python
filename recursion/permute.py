# Find all unique permutations of a given string

uniqueStrings = set()

def permute(a, l, r):

    if l == r:
        s = "".join(a)
        if s in uniqueStrings:
            return
        uniqueStrings.add(s)
        print(s, end=" ")
    
    for i in range(l, r + 1):
        a[i], a[l] = a[l], a[i]
        permute(a, l + 1, r)
        a[i], a[l] = a[l], a[i]

myString = "aabcd"
a = list(myString)
n = len(a)
permute(a, 0, n - 1)
        
