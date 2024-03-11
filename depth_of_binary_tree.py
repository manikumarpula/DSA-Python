class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self,root):
        self.root = root
     
    def depthTree(self,root):
        if root is None:
            return 0
        
        left = self.depthTree(root.left)
        right = self.depthTree(root.right)

        return max(left,right) + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
t = Tree(root)
    
depth = t.depthTree(root)
print(depth)