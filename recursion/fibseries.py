# Write a program to print fibonacci series upto nth


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


n = int(input())
for i in range(1, n+1):
    print(fib(i), end=" ")
