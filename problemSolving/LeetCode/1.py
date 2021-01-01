class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted = dict()
        position = []
        for i in range(len(nums)):
            if(target-nums[i] in wanted.keys()):
                position.append(i)
                position.append(wanted[target-nums[i]])
                return position
            else:
                wanted[nums[i]] = i