# Reverse a stack using resursion

def reverse_stack(stack):

    if len(stack) == 1:
        return
    
    temp = stack.pop()
    reverse_stack(stack)
    insert_element(stack, temp)

def insert_element(stack, value):

    if len(stack) == 0:
        stack.append(value)
        return

    temp = stack.pop()
    insert_element(stack, value)
    stack.append(temp)

stack = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10]
reverse_stack(stack)
print(stack)


