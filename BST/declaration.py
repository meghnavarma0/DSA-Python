class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()
    
    def size(self):
        return len(self.items)



class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            print("PREORDER: ", self.preorder_taversal(self.root, ""))
        if traversal_type == "inorder":
            print("INORDER: ", self.inorder_taversal(self.root, ""))

        if traversal_type == "postorder":
            print("POSTORDER: ", self.postorder_traversal(self.root, ""))

        if traversal_type == "levelorder":
            print("LEVELORDER: ", self.levelorder_traversal(self.root))

        if traversal_type == "reverselevelorder":
            print("REVERSE_LEVEL_ORDER : ", self.reverse_levelorder_traversal(self.root))

    def preorder_taversal(self, root, traversal):
        if root:
            traversal += str(root.value) + " "
            traversal = self.preorder_taversal(root.left, traversal)
            traversal = self.preorder_taversal(root.right, traversal)
        return traversal

    def postorder_traversal(self, root, traversal):
        if root:
            traversal = self.postorder_traversal(root.left, traversal)
            traversal = self.postorder_traversal(root.right, traversal)
            traversal += str(root.value) + " "
        return traversal

    def inorder_taversal(self, root, traversal):
        if root:
            traversal = self.inorder_taversal(root.left, traversal)
            traversal += str(root.value) + " "
            traversal = self.inorder_taversal(root.right, traversal)
        return traversal

    

    def levelorder_traversal(self, start):
        if start is None:
            return
        traversal = ""
        queue = Queue()
        queue.enqueue(start)

        while len(queue) > 0:
            traversal += str(queue.peek()) + " "
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_traversal(self, start):
        if start is None:
            return
        traversal = ""
        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)

            if node.left:
                queue.enqueue(node.left)

        while len(stack):
            traversal += str(stack.pop().value) + " "
        
        return traversal





tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.print_tree("preorder")
tree.print_tree("inorder")
tree.print_tree("postorder")
tree.print_tree("levelorder")
tree.print_tree("reverselevelorder")
