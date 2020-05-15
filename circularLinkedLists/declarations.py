class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class cicularLinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break

cList = cicularLinkedList()
cList.append(1)
cList.append(2)
cList.append(3)
cList.append(4)
cList.prepend(5)
cList.prepend(6)
cList.prepend(7)
cList.prepend(8)
cList.printList()
