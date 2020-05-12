# May challenge 2020

t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    result = 0
    a = 0
    k = 0
   
    
    for i in range(2, n + 1):
        
        c = 0
        
        #for j in range(i + i, n + 1, i + i):
        j = i + i
        prev = i
        while j <= n:
            
            if(arr[j] > arr[prev]):
                c += 1
                prev = j
                j += j
            else:
            
                j += prev
                
        if c >= result:
            result = c
            
            if arr[i] > arr[1]:
                result += 1
        
            
    if result >= 1:
        print(result)
    else:
        print(1)
        
    t -= 1
