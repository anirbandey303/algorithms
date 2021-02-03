class Solution:
    def hammingWeight(self, n: int) -> int:
        n = str(bin(n))
        total = 0
        for i in range(2,len(n)):
            if(n[i] == '1'):
                total += 1
        return total