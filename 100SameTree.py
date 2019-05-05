# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right

    
    def isSameTree(self, p, q):
        stack = deque()
        stack.append([p,q])
        while stack:
            n = stack.popleft()
            n1,n2 = n[0], n[1]
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            stack.append([n1.left, n2.left])
            stack.append([n1.right, n2.right])
        return True
    
        
            
