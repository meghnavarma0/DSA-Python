def insertVal(arr, val):
    if len(arr) == 0 or arr[-1] <= val:
        arr.append(val)
        return
    temp = arr[-1]
    arr.pop()
    insertVal(arr, val)
    arr.append(temp)

def sortArray(arr):
    if len(arr) == 1:
        return
    temp = arr[-1]
    arr.pop()
    sortArray(arr)
    insertVal(arr, temp)

arr = [0, 7, 2, 5, -2, -7]
sortArray(arr)
print(arr)

