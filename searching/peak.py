# A peak is defined a number that is greater than its neighbour/s. 
# in the array: 1 2 5 3 , 5 is peak element
# in 1 2 3 4, 4 is peak
# similarly, in 9, 8, 7, 6 --> 9

def findPeak(arr):

    if len(set(arr)) == 1:
        return -1

    n = len(arr)

    low = 0
    high = n - 1

    while low <= high:

        mid = low + (high - low) // 2 #Preventing integer overflow
        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid + 1] > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        if mid == 0:
            if arr[0] > arr[1]:
                return 0
            elif arr[1] > arr[0]:
                return 1
           
            
        elif mid == n - 1:
            if arr[n - 1] > arr[n - 2]:
                return n - 1
            return n - 2

    return -1


arr = [1, 3, 6, 3, 9, 7, 3, 2]
print(findPeak(arr)) # return 2 / 4 

arr2 = [2, 2, 2, 2, 2] 
print(findPeak(arr2)) # return -1
        