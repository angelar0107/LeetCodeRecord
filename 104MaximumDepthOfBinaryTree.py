# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    #recursive
    def maxDepth(self, root: TreeNode) -> int:
        if not  root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
    
    # iterative
    def maxDepth(self,root):
        if not root:
            return 0
        queue = deque([root])
        res = 0
        while queue:
            length = len(queue)
            res += 1
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
        
        
