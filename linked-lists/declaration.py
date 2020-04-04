class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append_val(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_ll(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        new_node = Node(data)

        temp = self.head
        while temp.data != prev_node:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp is None:
            print("The linked list is empty! Can't delete any :(")
            return

        if temp and temp.data is key:
            self.head = temp.next
            temp.next = None

        temp2 = self.head
        while temp.data != key:
            temp2 = temp
            temp = temp.next
        temp2.next = temp.next
        temp = None

    def delete_at_positon(self, pos):
        index = 0
        temp = self.head
        temp2 = temp
        if temp is None:
            print("The linked list is empty! Can't fulfil your plea")
            return
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        while index != pos and temp:
            temp2 = temp
            temp = temp.next
            index += 1
        if temp is None:
            print("This linked list is shorter than the given position.")
            temp = None
            return
        temp2.next = temp.next
        temp = None


a = LinkedList()
a.append_val("A")
a.append_val("B")
a.append_val("C")
a.append_val("Z")
a.prepend("E")
a.prepend("F")
a.prepend("G")
# a.insert_after_node("G", "G")
a.print_ll()
a.delete_at_positon(2)

# a.delete_node("A")
a.print_ll()
