class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        a = self.items.pop()
        return a

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        return True

    def print_stack(self):
        print("".join(self.items[::-1]))


s = Stack()
print(s.isEmpty())
str1 = "Hello"
for i in str1:
    s.push(i)


s.print_stack()
print(s.isEmpty())

while(not s.isEmpty):
    print(s.pop())
