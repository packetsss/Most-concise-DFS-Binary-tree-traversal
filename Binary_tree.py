"""
My binary tree:
         1
       /   \
      2     3
     / \   / \
    4   5 6   7

Pre-order:      1 -> 2 -> 4 -> 5 -> 3 -> 6 -> 7
    Start from root, keep going to left, if can't go left anymore, move one to right

In-order:       4 -> 2 -> 5 -> 1 -> 6 -> 3 -> 7
    Start from deepest left node, then move to the right

Post-order:     4 -> 2 -> 5 -> 6 -> 3 -> 7 -> 1
    I forgot -.-
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = Node(root)

    def pre(self, node):
        if node:
            return f"{node.value} -> {self.pre(node.left)}{self.pre(node.right)}"
        return ""

    def in_(self, node):
        if node:
            return f"{self.in_(node.left)}{node.value} -> {self.in_(node.right)}"
        return ""

    def post(self, node):
        if node:
            return f"{self.post(node.left)}{self.post(node.right)}{node.value} -> "
        return ""


tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


print(tree.pre(tree.root))
print(tree.in_(tree.root))
print(tree.post(tree.root))

