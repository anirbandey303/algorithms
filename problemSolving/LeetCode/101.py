#101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetricCheck(self, left, right):
        if(left == None or right == None):
            return left == right
        if(left.val != right.val):
            return False
        return self.isSymmetricCheck(left.left, right.right) and self.isSymmetricCheck(left.right, right.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if(root == None):
            return True
        return self.isSymmetricCheck(root.left,root.right)
    