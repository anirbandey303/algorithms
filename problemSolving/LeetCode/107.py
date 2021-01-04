# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if(root is None):
            return []
        queue = []
        result = []
        queue.append(root)
        while(queue):
            nodes = []
            size = len(queue)
            for i in range(size):
                n = queue.pop(0)
                if(n.left):
                    queue.append(n.left)
                if(n.right):
                    queue.append(n.right)
                nodes.append(n.val)
            result.insert(0, nodes)
        return result