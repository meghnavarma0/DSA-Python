from declaration import LinkedList


class llExtra(LinkedList):

    def count_occurences_iterative(self, data):
        freq = 0
        curr = self.head

        while curr:
            if curr.data == data:
                freq += 1
            curr = curr.next

        print("Frequency of", data, "is", freq)

    def count_occurences_recursive(self, data, node):
        if not node:
            result = 0

        elif node.data == data:
            result = 1 + self.count_occurences_recursive(data, node.next)
        else:
            result = 0 + self.count_occurences_recursive(data, node.next)
        return result


a = llExtra()
a.append_val(1)
a.append_val(3)
a.append_val(1)
a.append_val(4)
a.append_val(1)
a.append_val(5)
a.append_val(1)

# a.count_occurences_iterative(6)
print(a.count_occurences_recursive(1, a.head))
