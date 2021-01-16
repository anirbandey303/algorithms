class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        nums = [0, 1]
        for k in range(2, n + 1):
            m = k // 2
            if k & 1 == 0:
                nums.append(nums[m])
            else:
                nums.append(nums[m] + nums[m + 1])
        return max(nums)