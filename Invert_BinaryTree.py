#Problem is to invert the tree
#Initially Convert left and right childrens through recursion
#So that parents of respected childs change their positions.

from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self,root):
        self.root = root

    def traversal(self,root):
        result = []
        queue = deque([root])
        while queue:
            curr_node = queue.popleft()
            result.append(curr_node.val)

            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        return result
    def invertTree(self,root):
        if root is None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
t = Tree(root)
k = t.traversal(t.root)
print(k)
t.invertTree(t.root)
k = t.traversal(t.root)
print(k)

    