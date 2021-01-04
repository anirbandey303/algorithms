# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    theList = None
    
    def addToList(self,value):
        if(self.theList == None):
            newNode = ListNode(value)
            self.theList = newNode
        else:
            temp = self.theList
            while(temp.next):
                temp=temp.next
            newNode = ListNode(value)
            temp.next = newNode

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1 = l1
        temp2 = l2
        while(temp1 != None and temp2 != None):
            if(temp1.val <= temp2.val):
                self.addToList(temp1.val)
                temp1 = temp1.next
            else:
                self.addToList(temp2.val)
                temp2 = temp2.next
        while(temp1):
            self.addToList(temp1.val)
            temp1 = temp1.next
        while(temp2):
            self.addToList(temp2.val)
            temp2 = temp2.next
        return self.theList
        