#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(arr, k, n):
    t = [[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            if(arr[i-1] <= j):
                t[i][j] = max(arr[i-1] + t[i][j-arr[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][k]

if __name__ == '__main__':
    

    t = int(input())

    while t:

        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(arr, k, n)

        print(result)

        t -= 1


