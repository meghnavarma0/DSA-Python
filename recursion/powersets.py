# Given a string, find all the strings that can be produced using it.

def solve(ip, op):
    #print("input", ip)
    # Base condition : 
    if len(ip) == 0:
        print(" ".join(op))
        return

    op1 = op[::]
    op2 = op[::]

    op2.append(ip[0]) 
   
    solve(ip[1 : ], op1)
    solve(ip[1: ], op2)

s = list(input())
solve(s, [])