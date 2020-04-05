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

    def len_iterative(self):
        count = 1
        temp = self.head
        if temp is None:
            count = 0
            print("The linked list is empty.")
            return

        while temp.next is not None:
            temp = temp.next
            count += 1

        print("The length of linked list is :", count)

    def len_recursive(self, head):
        if head is None:
            return 0
        return 1 + self.len_recursive(head.next)

    def return_head(self):
        return self.head

    def swap_nodes(self, key1, key2):

        if key1 == key2:
            return
        prev1 = None
        curr1 = self.head

        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next

        prev2 = None
        curr2 = self.head

        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next
        if not curr1 or not curr2:
            return

        if prev1:

            prev1.next = curr2

        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        curr1.next, curr2.next = curr2.next, curr1.next

    def reverse_iterative(self):
        prev = None
        current = self.head

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(self.head, None)


a = LinkedList()
a.append_val("A")
a.append_val("B")
a.append_val("C")
a.append_val("Z")
a.prepend("E")
a.prepend("F")
a.prepend("G")
# a.insert_after_node("G", "G")
# a.print_ll()
# a.len_iterative()
# p = a.len_recursive(a.return_head())
# print(p)
# a.delete_at_positon(2)

# a.delete_node("A")
a.print_ll()
# a.len_iterative()
# print(a.len_recursive(a.head))
# a.swap_nodes("F", "G")
a.reverse_recursive()
a.print_ll()
