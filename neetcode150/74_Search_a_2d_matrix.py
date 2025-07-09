"""74. Search a 2D Matrix
Solved
Medium
Topics
premium lock icon
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        totalRows = len(matrix)
        totalColumns = len(matrix[0])

        top = 0
        bottom = totalRows -1

        while(top<=bottom):
            middleRow = (top + bottom) // 2
            if(target >= matrix[middleRow][0] and target <= matrix[middleRow][-1]):
                break
            elif(target > matrix[middleRow][-1]):
                top = middleRow + 1
            else:
                bottom = middleRow - 1

        row = (top + bottom) // 2
   
        left, right = 0, totalColumns - 1

        while(left <= right):
            mid = (left + right) // 2
            if(target == matrix[row][mid]):
                return True
            elif(target > matrix[row][mid]):
                left = mid + 1
            else:
                right = mid - 1
        return False