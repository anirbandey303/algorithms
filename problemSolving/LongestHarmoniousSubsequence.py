class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        myMap = dict()
        for i in nums:
            if(i in myMap.keys()):
                myMap[i] += 1
            else:
                myMap[i] = 1
        for k in myMap.keys():
            if(k+1 in myMap.keys()):
                result = max(result, myMap[k] + myMap[k+1])
        return result