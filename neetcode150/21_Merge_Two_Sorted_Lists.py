"""
21. Merge Two Sorted Lists
Solved
Easy
Topics
premium lock icon
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, value):
        newNode = ListNode(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return self.head
        currentNode = self.tail
        # while(currentNode.next):
        #     currentNode = currentNode.next
        currentNode.next = newNode
        self.tail = newNode
        return self.head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        finalList = LinkedList()
        curr1 = list1
        curr2 = list2

        if not curr1 and not curr2:
            return None
        if not curr1:
            return curr2
        if not curr2:
            return curr1

        while(True):
            # both lists have nodes
            if(curr1 and curr2):
#                finalList.insertNode(min(curr1.val, curr2.val))
                if(curr1.val<curr2.val):
                    finalList.insertNode(curr1.val)
                    curr1 = curr1.next
                else:
                    finalList.insertNode(curr2.val)
                    curr2 = curr2.next
            elif(curr1 is None and curr2 is not None):
                # add all elements of list2
                finalList.insertNode(curr2.val)
                curr2 = curr2.next
            elif(curr1 is not None and curr2 is None):
                # addd all elements of list1
                finalList.insertNode(curr1.val)
                curr1 = curr1.next
            else:
                break


        return finalList.head