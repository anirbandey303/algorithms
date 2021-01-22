class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        a = len(nums) - k
        myStack = []
        for num in nums:
            while myStack and num < myStack[-1] and a > 0:
                myStack.pop()
                a -= 1
            myStack.append(num) 
        return myStack[:k]