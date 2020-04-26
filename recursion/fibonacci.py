# Write a program to print nth fibonacci number of a sequence


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


t = int(input())
while t:
    n = int(input())
    print(fib(n))

    t -= 1
