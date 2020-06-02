# Given an array, find the first greater element to right
# eg. arr = [4, 2, 6, 9, 7] --> [6, 6, 9, -1, -1]


def firstGreaterToRight(arr):
    stack = []
    result = []
    for i in range(len(arr) - 1, -1, -1):
        if(len(stack) == 0):
            result.append(-1)
        elif(stack[-1] > arr[i]):
            result.append(stack[-1])
        elif stack[-1] <= arr[i]:
            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()

            if len(stack) == 0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(arr[i])
    return result[::-1]

arr = [4, 2, 6, 9, 7]
print(firstGreaterToRight(arr))
            