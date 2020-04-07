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
