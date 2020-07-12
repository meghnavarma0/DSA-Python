# Given an array and q queries with lower and upper limit of range.
# For each query, find the maximum in the for the given range.

import sys
seg = [0 for i in range(4 * 100005)]
def build(ind, low, high):
    if low == high:
        seg[ind] = arr[low]
        return
    mid = (low+high)//2
    build(2*ind+1, low, mid)
    build(2*ind+2, mid+1, high)
    seg[ind] = max(seg[2*ind+1], seg[2*ind+2])

def query(ind, low, high, l, h):
    if low >= l and high <= h:
        return seg[ind]
    if low > h or high < l:
        return -sys.maxsize+1
    mid = (low + high)//2
    left = query(2*ind+1, low, mid, l, h)
    right = query(2*ind+2, mid+1, high, l, h)
    return max(left, right)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    build(0, 0, n-1)
    q = int(input())
    while q:
        l,h = list(map(int, input().split()))
        print(query(0, 0, n-1, l, h))
        q -= 1
