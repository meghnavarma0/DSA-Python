# Give an array depicting a number. Add 1 such that the arithmetic result is correct
# eg if arr = [1, 4, 9] => [1, 5, 0]
# if arr = [9, 9, 9] => [1, 0, 0, 0]


def arbitrary(arr):
    i = len(arr) - 1

    while i >= 0:
        if arr[i] + 1 > 9:
            arr[i] = 0
            i -= 1
        else:
            arr[i] += 1
            return
    if i == -1:
        arr.insert(0, 1)
        return


arr = [9, 9, 9]
arbitrary(arr)

print(arr)
