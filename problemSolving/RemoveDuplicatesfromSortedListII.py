# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        temp = head
        while(temp and temp.next):
            if(temp.val != temp.next.val):
                prev = temp
                temp = temp.next
            else:
                while(temp.next and temp.val == temp.next.val):
                    temp = temp.next
                temp = temp.next
                if(prev):
                    prev.next = temp
                else:
                    head = temp
        return head