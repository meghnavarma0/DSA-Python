def isPrime(n):
    for i in range(2, int(pow(n, 0.5) + 1)):
        if n % i == 0:
            return False
    return True

def SieveOfEratosthenes(a, b): 
    allPrimes = []
    
    arrPrimes = [True for i in range(b+1)] 
    p = 2
    while (p * p <= b): 
        
        if (arrPrimes[p] == True): 
           
            for i in range(p * p, b+1, p): 
                arrPrimes[i] = False
        p += 1
      
    
    for p in range(a, b+1): 
        if arrPrimes[p]: 
            allPrimes.append(p)
    return allPrimes

a, b = list(map(int, input().split()))
arr = SieveOfEratosthenes(a, b)

arr2 = set()
n = len(arr)
for i in range(n):
    for j in range(n):
        if i != j:
            arr2.add(str(arr[i]) + str(arr[j]))
arr2 = list(map(int, arr2))

res = []
for i in arr2:
    if isPrime(i):
        res.append(i)



a3 = min(res)
b3 = max(res)
l = len(res)

def nthFibonacci(a, b, l):
    s = 0
    for i in range(l-2):
        s = a + b
        a = b
        b = s
    return s

print(nthFibonacci(a3, b3, l))


