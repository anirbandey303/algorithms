# BST - Level order traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class Solution:
    def insert(self, root, data):
        if(root is None):
            return Node(data)
        else:
            if(data <= root.data):
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root
    def levelOrder(self,root):
        to_be_searched = []
        has_been_searched = ''
        to_be_searched.append(root)
        while(to_be_searched):
            currNode = to_be_searched.pop(0)
            if(currNode.left):
                to_be_searched.append(currNode.left)
            if(currNode.right):
                to_be_searched.append(currNode.right)
            has_been_searched += str(currNode.data) + ' '
        print(has_been_searched)
        
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
