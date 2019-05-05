# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        flag = 1
        res = []
        queue = deque([root])
        while queue:
            length = len(queue)
            temp = []
            for _ in range(length):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag == -1:
                temp = temp[:: - 1]
            if temp:
                res.append(temp)
            flag = -flag
        return res
