def findFloor(arr, x):

    l = 0
    h = len(arr) - 1
    mid = None
    result = None

    while l <= h:
        mid = (l + h) // 2
        if arr[mid] == x:
            return arr[mid]
        elif x < arr[mid]:
            h = mid - 1
        else:
            result = arr[mid]
            l = mid + 1
    return result

arr = [1, 2, 4, 7, 9, 13, 18, 20]
for i in range(int(input("Enter no. of test cases : "))):
    n = int(input("Enter no."))
    print("Floor : ", findFloor(arr, n))