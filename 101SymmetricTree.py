# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.sym(root.left, root.right)
    
    def sym(self,left,right):
        if not left and not right:
            return True
        if not right or not left:
            return False
        return left.val == right.val and self.sym(left.left,right.right) and self.sym(right.left,left.right)
