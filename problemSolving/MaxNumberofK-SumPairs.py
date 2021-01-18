class Solution:
    def decrement(self, num, myMap):
        myMap[num] -= 1
        return myMap
        
    def addIncr(self, num, myMap):
        if num in myMap.keys():
            myMap[num] += 1
        else:
            myMap[num] = 1
        return myMap
        
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        myMap = dict()
        for i in range(n):
#             if sum doesnt exsist
#                 add num to list
            
#                 if num exists
#                 increment count
            
#            elif sum exists and val>0
#            decrement counts
#            pop from array
#            5 - 2 = 3    
    
            if k-nums[i] in myMap.keys() and myMap[k-nums[i]] > 0:
                myMap = self.decrement(k-nums[i], myMap)
                count += 1
            else:
                myMap = self.addIncr(nums[i], myMap)
            
        return count

#################################################################################


class Solution:
       
    def maxOperations(self, nums: List[int], k: int) -> int:
        p1 = 0
        p2 = len(nums)-1
        count = 0
        nums.sort()
        while(p1<p2):
            if(nums[p1] + nums[p2] > k):
                p2 -= 1
            elif(nums[p1] + nums[p2] < k):
                p1 += 1
            else:
                count += 1
                p1 += 1
                p2 -= 1
        return count