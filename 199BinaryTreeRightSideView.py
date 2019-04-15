# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    
    
#BFS solution
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result, queue = [],deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == length - 1:
                    result.append(node.val)
        return result
        
#DFS solution
    def rightSideView(self,root):
        result = []
        self.depth = 0
        self.dfs(root,1,result)
        return result
        
        
    def dfs(self,root,count,result):
        if not root:
            return
        if count > self.depth:
            self.depth +=1
            result.append(root.val)
        self.dfs(root.right,count + 1,result)
        self.dfs(root.left,count + 1,result)
            
        
