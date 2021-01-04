class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        numbers = dict()
        
        for i in nums:
            if(i in numbers.keys()):
                numbers[i] += 1
            else:
                numbers[i] = 1
        
        for k in numbers.keys():
            if (numbers[k] == 1):
                return k