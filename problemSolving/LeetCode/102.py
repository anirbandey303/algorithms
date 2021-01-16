# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = list()
        if(root == None):
            return []
        else:
            queue.append(root)
        finalList = list()
        lcount = 0
        while(queue):
            nexts = list()
            lcount = len(queue)
            for i in range(lcount):
                node = queue.pop(0)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
                nexts.append(node.val)
            finalList.append(nexts)
        return finalList