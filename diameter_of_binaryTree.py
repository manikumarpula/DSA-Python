#The problem is to return the diameter of a Binary Tree
#The diameter of a binary tree is defined as the longest between two nodes in entire tree


class treeNode:
    diameter = 0

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self):
        root = treeNode(1)
        root.left = treeNode(2)
        root.right = treeNode(3)
        root.left.left = treeNode(4)
        root.left.right = treeNode(5)
        root.left.left.left = treeNode(6)
        return root

    def diameter_of_tree(self, node):
        self.height(node)
        return self.diameter - 1

    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

        dia = left_height + right_height + 1
        self.diameter = max(dia, self.diameter)

        return max(left_height, right_height) + 1

t = treeNode(0)
root = t.insert()
diameter = t.diameter_of_tree(root)
print(diameter)
