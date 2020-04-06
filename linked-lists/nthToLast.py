from declaration import LinkedList


class LinkedExtra (LinkedList):

    def nThToLast(self, n):
        total_length = self.len_iterative()
        curr = self.head
        while curr:
            if n == total_length:
                print(curr.data)
                return curr
            curr = curr.next
            total_length -= 1

        print("Wrong Input")

    def nThToLast2(self, n):
        p = self.head
        q = self.head
        total_length = self.len_iterative()
        if(n > total_length):
            print("n cannot possess value greater than the length of the linked list.")
            return

        count = 0
        while q and count < n:
            q = q.next
            count += 1

        while p and q:
            p = p.next
            q = q.next

        print(p.data)


a = LinkedExtra()
a.append_val("A")
a.append_val("B")
a.append_val("C")
a.append_val("D")
a.append_val("E")
a.append_val("F")
a.append_val("G")

a.print_ll()

a.nThToLast2(3)
