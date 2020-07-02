# Given a string, permute the case of all letter in the string.
# a1B2 -->
# a1b2 a1B2 A1b2 A1B2

def solve(ip, op, result):

    if not ip:
        result.append("".join(op))
        return

    if ip[0].isdigit():
        solve(ip[1:], op[::] + [ip[0]], result)

    elif ip[0].isalpha():
        op1 = op[::] + [ip[0].lower()]
        op2 = op[::] + [ip[0].upper()]

        ip = ip[1:]
        solve(ip, op1, result)
        solve(ip, op2, result)

if __name__ == "__main__":
    s = list(input())
    ip = s[::]
    op = []
    result = []
    solve(ip, op, result)
    print(" ".join(result))

