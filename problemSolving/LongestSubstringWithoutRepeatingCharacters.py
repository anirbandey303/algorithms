#  p w w k e w
#      i
#  j
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0 or s == None):
            return 0
        i = 0
        j = 0
        maximum = 0
        mySet = set()
        while(i < len(s)):
            n = s[i]
            while(n in mySet):
                mySet.remove(s[j])
                j += 1
            mySet.add(n)
            maximum = max(maximum, i-j+1)
            i+=1
        return maximum