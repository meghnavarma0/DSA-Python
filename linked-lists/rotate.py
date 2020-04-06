from declaration import LinkedList


class Rotate(LinkedList):

    def rotate(self, n):
        total_length = self.len_iterative()
        n = n % total_length
        if n == 0:
            return
        p = self.head
        q = self.head
        count = 0

        while count < n - 1:
            q = q.next
            count += 1

        self.head = q.next
        temp = self.head
        q.next = None

        while temp.next:
            temp = temp.next

        temp.next = p


a = Rotate()
a.append_val(1)
a.append_val(2)
a.append_val(3)
a.append_val(4)
a.append_val(5)
a.append_val(6)
a.print_ll()

a.rotate(0)
a.print_ll()
