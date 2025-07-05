"""42. Trapping Rain Water
Solved
Hard
Topics
premium lock icon
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        
        maxLeft = [-1] * n
        maxRight = [-1] * n
        minLR = [-1] * n
        
        for i in range(len(height)):
            if i == 0:
                maxLeft[0] = 0
            else:
                maxLeft[i] = max(maxLeft[i-1], height[i-1])
        for i in reversed(range(len(height))):
            if i == len(height)-1:
                maxRight[i] = 0
            else:
                maxRight[i] = max(maxRight[i+1], height[i+1])
        for i in range(len(height)):
            volume = min(maxLeft[i], maxRight[i]) - height[i]
            if(volume <= 0):
                minLR[i] = 0
            else:
                minLR[i] = volume
        return sum(minLR)