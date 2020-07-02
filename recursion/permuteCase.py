# Given a string in lowerCase, print all permutations of it in both cases.

# ab --> ab aB Ab AB

def solve(ip, op):

    if not ip:
        print("".join(op))
        return

    op1 = op[::] + [ip[0].lower()]
    op2 = op[::] + [ip[0].upper()]

    ip = ip[1:]

    solve(ip, op1)
    solve(ip, op2)

if __name__ == "__main__":

    s = list(input())
    ip = s[::]
    op = []
    solve(ip, op)


