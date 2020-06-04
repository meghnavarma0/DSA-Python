

def StockSpan(arr, flag):
    stack = []
    n = len(arr)
    result = []
    pseudoIndex = None
    start = None
    stop = None
    step = None
    # flag --> True --> NSL --> Nearest Smaller to Left
    # flag --> Flase --> NSR --> Nearest Smaller to Right
    if flag:
        pseudoIndex = -1
        start = 0
        stop = n
        step = +1
    else:
        pseudoIndex = n
        start = n - 1
        stop = -1
        step = -1


    for i in range(start, stop, step):
        if len(stack) == 0:
            result.append(pseudoIndex)
        elif stack[-1][0] < arr[i]:
            result.append(stack[-1][1])
        elif stack[-1][0] >= arr[i]:
            while len(stack) > 0 and stack[-1][0] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(pseudoIndex)
            else:
                result.append(stack[-1][1])
        stack.append((arr[i], i))
   
    return result

arr = [6, 2, 5, 4, 5, 1, 6]
left = StockSpan(arr, True)
right = StockSpan(arr, False)[::-1]
width = []
for i in range(len(arr)):
    width.append(right[i] - left[i] - 1)
area = []
for i in range(len(arr)):
    area.append(arr[i] * width[i])
print(right)
print(left)
print(width)
print(area)
print(max(area))