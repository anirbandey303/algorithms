"""3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set()
        l = 0
        maxLength = 0

        # keep iterating the right pointer
        for r in range(len(s)):
            while(s[r] in substr):
                substr.remove(s[l])
                l+=1
            substr.add(s[r])
            maxLength = max(maxLength, r-l+1)
        
        return maxLength
