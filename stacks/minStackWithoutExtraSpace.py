# Develop push, pop, top, and minEl functions for a min-stack
stack = []
minele = 0
def push(x):
    global minele
    if len(stack) == 0:
        minele = x
        stack.append(x)
    else:
        if x >= minele:
            stack.append(x)
        else:
            stack.append(2 * x - minele)
            minele = x

def pop():
    global minele
    if len(stack) == 0:
        return -1
    else:
        if stack[-1] < minele:
            a = minele
            minele = 2 * minele - stack[-1]
            stack.pop()
            return a
        else:
            a = stack.pop()
            return a

def top():
    global minele
    if len(stack) == 0:
        return -1
    else:
        if stack[-1] < minele:
            return minele
        else:
            return stack[-1]

def minEle():
    global minele
    if len(stack) == 0:
        return -1
    return minele

push(5)
print(stack)
print(minele)

push(4)
print(stack)
push(6)
print(stack)
push(8)
print(stack)
push(2)
print(stack)
push(1)
print(stack)
print(minEle())
pop()
print(minEle())
pop()
print(minEle())




