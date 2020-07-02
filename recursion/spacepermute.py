# Given a string, print output as such: 
# abc --> abc a-bc ab-c a-b-c

def solve(ip, op):
    
    if not ip:
        print("".join(op))
        return

    op1 = op[::]
    op2 = op[::]

    op1 += [ip[0]]
    op2 += ["-", ip[0]]

    
    solve(ip[1:], op1)
    solve(ip[1:], op2)
    return



if __name__ == "__main__":
    s = input()
    ip = list(s)
    op = []

    op += [ip[0]]
    del ip[0]

    solve(ip, op)

