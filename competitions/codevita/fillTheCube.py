def nsl(arr):
    n = len(arr)
    stack = []
    result = []
    for i in range(n):
        if not stack:
            result.append(-1)
        elif stack[-1][0] < arr[i]:
            result.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if stack:
                result.append(stack[-1][1])
            else:
                result.append(-1)
        stack.append((arr[i], i))
    return result

def nsr(arr):
    n = len(arr)
    stack = []
    result = []
    for i in range(n-1, -1, -1):
        if not stack:
            result.append(n)
        elif stack[-1][0] < arr[i]:
            result.append(stack[-1][1])
        else:
            while stack and stack[-1][0] >= arr[i]:
                stack.pop()
            if stack:
                result.append(stack[-1][1])
            else:
                result.append(n)
        stack.append((arr[i], i))
    return result[::-1]



def solve(matrix, n):
    
    arr1 = [0]*n
    arr2 = [0]*n
    
    for i in range(n):
        for j in range(n):
            
            if matrix[i][j] == "D":
                arr1[i] += 1
                
            if matrix[j][i] == "D":
                arr2[i] += 1

    
    left1 = nsl(arr1)
    right1 = nsr(arr1)
    width1 = [ right1[i] - left1[i] - 1 for i in range(n)]
    ans1 = [min(arr1[i], width1[i]) for i in range(n)]
    final1 = max(ans1)
    


    left2 = nsl(arr2)
    right2 = nsr(arr2)
    width2 = [ right2[i] - left2[i] - 1 for i in range(n)]
    ans2 = [min(arr2[i], width2[i]) for i in range(n)]
    final2 = max(ans2)

    

    #print("finals", final1, final2)

    return max(final1, final2)



n = int(input())
t = n
matrix = []
while t:
    arr = input().split()
    matrix.append(arr)
    
    t -= 1
print(solve(matrix, n))
