import math


# carry = 1 

# 2 --- 4 --- 3
# 5 --- 6 --- 4
# --------------------
# 7 --- 0 --- 8


# carry  = (9+7)/10
# 9 --- 3 --- 8 --- none
# 7 --- 1 --- 9 --- none
# ----------------------
# 6(9+7%10) --- 5 ---  --- 1


# carry = 1

# 9 --- 1 --- 7 --- 1 --- n 
# 8 --- 3 --- 4 --- 0 --- 9 --- 9 --- n
# ----------------------------------------------
# 7 --- 5 --- 1 --- 2 --- 0 ~~~ 0 ~~~ 1




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertNode(self,myList,value):
        if(myList == None):
            newNode = ListNode(value)
            myList = newNode
            return myList
        else:
            temp = myList
            while(temp.next):
                temp = temp.next
            newNode = ListNode(value)
            temp.next = newNode
            return myList
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = l1
        list2 = l2
        carry = 0
        finalList = None
        while(list1 and list2):
            sums = list1.val + list2.val + carry
            digit = (sums)%10
            carry = sums//10
            finalList = self.insertNode(finalList,digit)
            list1 = list1.next
            list2 =  list2.next
        while(list1):
            sums = list1.val + carry
            digit = (sums)%10
            carry = sums//10
            finalList = self.insertNode(finalList,digit)
            list1 = list1.next
        while(list2):
            sums = list2.val + carry
            digit = (sums)%10
            carry = sums//10
            finalList = self.insertNode(finalList,digit)
            list2 = list2.next
        if(carry>0):
            finalList = self.insertNode(finalList, carry)
        return finalList