# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if(head == None):
            return False
        slowPointer = head
        fastPointer = head.next
        
        while(slowPointer != fastPointer):
            if(fastPointer == None or fastPointer.next == None):
                return False
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        return True