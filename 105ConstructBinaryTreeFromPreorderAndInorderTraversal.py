# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        root = preorder[0]
        for i in range(len(inorder)):
            if inorder[i] == root:
                break
        left = self.buildTree(preorder[1:i + 1], inorder[:i])
        right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        root = TreeNode(root)
        root.left = left
        root.right = right
        return root

            
