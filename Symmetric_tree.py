# Definition for a binary tree node.
# class TreeNode:
def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root.left,root.right])
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if left == None and right == None:
                continue
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True