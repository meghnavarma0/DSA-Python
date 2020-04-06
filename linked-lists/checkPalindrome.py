from declaration import LinkedList


class PalindromeListCheck(LinkedList):
    # The string method.
    def checkPal(self):
        s = ""
        p = self.head

        while p:
            s += p.data
            p = p.next

        if s == s[:: -1]:
            print("The Linked List is palindromic! Wohoo!!!")
            return
        print("Linked List is not palindromic, sad! :(")

    # The stack way!
    def checkPal2(self):
        stack = []
        temp = self.head

        while temp:
            stack.append(temp.data)
            temp = temp.next

        temp = self.head
        while temp:
            data = stack.pop()
            if temp.data != data:
                print("Not a palindromic linked list.")
                return
            temp = temp.next
        print("Linked list is palindromic")

    def checkPal3(self):
        list_of_nodes = []
        temp = self.head
        i = 0

        while temp:
            list_of_nodes.append(temp)
            temp = temp.next
            i += 1
        p = self.head
        count = 1
        while count <= i // 2 + 1:
            if list_of_nodes[-count].data != p.data:
                print("Not a palindromic linkedlist")
                return
            p = p.next
            count += 1
        print("Palindromic linked list!")


a = PalindromeListCheck()
a.append_val("A")
a.append_val("B")
a.append_val("B")
a.append_val("L")

a.checkPal()
a.checkPal2()
a.checkPal3()
