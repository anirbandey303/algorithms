class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if(len(arr) == 0 or len(arr) == 1):
            return True
        arr.sort()
        diff = abs(arr[0] - arr[1])
        for i in range(len(arr)-1):
            if(abs(arr[i] - arr[i+1]) != diff):
                return False
        return True