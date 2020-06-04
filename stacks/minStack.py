s = []
ss = []
def push(a):
    s.append(a)
    if len(ss) == 0 or ss[-1] >= a:
        ss.append(a)

def popElement():
    if len(s) == 0:
        return -1
    else:
        temp = s.pop()
        if temp == ss[-1]:
            ss.pop()

def stackMin():
    if len(s) == 0:
        return -1
    return ss[-1]

push(18)
push(19)
print(s)
print(stackMin())
push(29)
print(s)
print(stackMin())
push(15)
print(s)
print(stackMin())
popElement()
push(16)
print(s)
print(stackMin())