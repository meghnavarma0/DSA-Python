
def ugly(n):
    arr = [1]

    i2, i3, i5 = 0, 0, 0

    next_mul_of_2 = arr[i2] * 2
    next_mul_of_3 = arr[i3] * 3
    next_mul_of_5 = arr[i5] * 5

    while len(arr) < n:
        arr.append(min(next_mul_of_2, next_mul_of_3, next_mul_of_5))
        if arr[-1] == next_mul_of_2:
            i2 += 1
            next_mul_of_2 = arr[i2] * 2
        if arr[-1] == next_mul_of_3:
            i3 += 1
            next_mul_of_3 = arr[i3] * 3
        if arr[-1] == next_mul_of_5:
            i5 += 1
            next_mul_of_5 = arr[i5] * 5
    return arr[-1]


for i in range(1, 10):
    print(ugly(i))
