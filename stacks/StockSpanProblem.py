# Given an array, find the number of consecutive elements less than or equal to it to its left.
# arr = [100, 80, 60, 70, 60, 75, 85]
# ans = [ 1 , 1 , 1 , 2 , 1 , 4 , 6 ]
# Variation of nearest greater to left: 

def StockSpan(arr):
    stack = []
    result = []

    for i in range(len(arr)):
        if len(stack) == 0:
            result.append(-1)
        elif stack[-1][0] > arr[i]:
            result.append(stack[-1][1])
        elif stack[-1][0] <= arr[i]:
            while len(stack) > 0 and stack[-1][0] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1][1])
        stack.append((arr[i], i))
    print(result)
    for i in range(len(result)):
        result[i] = i - result[i]

    return result

arr = [100, 80, 60, 70, 60, 75, 85]
print(StockSpan(arr))