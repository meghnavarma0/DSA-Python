# Write a program to delete the middle element of a stack

def delete_mid(stack, k):
    # Base Condition
    if k == 1:
        stack.pop()
        return

    # Hypothesis
    temp = stack.pop()
    delete_mid(stack, k - 1)
    
    # Induction
    stack.append(temp)

arr = [1, 2, 3, 4, 5]
k = len(arr) // 2 + 1
delete_mid(arr, k)
print(arr)
