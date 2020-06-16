# Partition an array into two equal sum arrays.
# Find whether or not the partition is possible.

def partition(arr, s, i, ans):
    if i >= len(arr) or s < 0:
        return False
    if s == 0:
        return True
    ans.append(arr[i])
    if partition(arr, s - arr[i], i + 1, ans):
        return True
    ans.pop()
    return partition(arr, s, i + 1, ans)


def find(arr):
    s = sum(arr)
    ans = []
    isPossible = s & 1 == 0 and partition(arr, s//2, 0, ans)
    if isPossible:
        return(ans)
    else:
        return("Partition is not possible!")

arr = [1, 2, 3, 2, 8, 4]
print(find(arr))