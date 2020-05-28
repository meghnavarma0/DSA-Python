def binarySearch(arr, k):

    if k > len(arr):
        return -1
    
    start = min(arr)
    end = sum(arr)

    result = -1

    while start <= end:

        mid = start + (end - start) // 2

        if isValid(arr, k, mid):
            result = mid
            end = mid - 1
        
        else:
            start = mid + 1

    return result

def isValid(arr, k, mid):

    n = len(arr)

    intermediateSum = 0

    numberOfStudentsRequired = 1

    for i in range(0, n):

        intermediateSum += arr[i]

        if intermediateSum > mid:

            numberOfStudentsRequired += 1

            intermediateSum = arr[i]
        
        if numberOfStudentsRequired > k:
            return False

    return True

arr = [10, 20, 30, 40]
k = 2
print(binarySearch(arr, k))
