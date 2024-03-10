#This Program return height of a binary Tree
#empty node height is 0
#tree having one node is 1
#Height is defined as maximum no of nodes between leaf node and root node 

class treeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def height_tree(node):
    if node is None:
        return 0
    else:
        left_height = height_tree(node.left)
        right_height = height_tree(node.right)
    return max(left_height,right_height) + 1
root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(3)
root.left.left = treeNode(4)
root.left.right = treeNode(5)

height_tree(root)
print(height_tree(root))