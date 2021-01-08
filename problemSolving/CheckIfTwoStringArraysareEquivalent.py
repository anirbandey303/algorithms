class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ""
        string2 = ""
        for i in word1:
            string1 += i
        for j in word2:
            string2 += j
        return string1 == string2