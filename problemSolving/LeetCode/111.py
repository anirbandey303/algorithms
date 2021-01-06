# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(root == None):
            return 0
        queue = []
        queue.append(root)
        depth  = 0
        while(queue):
            numberOfNodes = len(queue)
            while(numberOfNodes > 0 ):
                node = queue.pop(0)
                if(node.left == node.right == None):
                    return depth+1
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
                numberOfNodes -= 1
            depth+=1