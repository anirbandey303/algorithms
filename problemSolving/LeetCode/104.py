# Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if(left>right):
            return 1+left
        else:
            return 1+right