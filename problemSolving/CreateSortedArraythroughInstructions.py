from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        sortedList = SortedList()
        totalCost = 0
        modulo  = 10 ** 9 + 7
        
        for i in instructions:
            left = sortedList.bisect_left(i)
            right = len(sortedList) - sortedList.bisect_right(i)
            totalCost += min(left,right)
            totalCost %= modulo
            sortedList.add(i)
        return totalCost