"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = deque()
        queue.append(root)
        while queue:
            length = len(queue)
            for i in range(length):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                if i == length - 1:
                    continue
                curr.next = queue[0]
        return root


# Constant extre space solution
    def connect2(self,root):
        if not root:
            return
        dummy = root
        nextlevel = level = Node(0,None,None,None)
        while root:
            if root.left:
                level.next = root.left
                level = level.next
            if root.right:
                level.next = root.right
                level = level.next
            root = root.next
        self.connect2(nextlevel.next)
        return dummy        
