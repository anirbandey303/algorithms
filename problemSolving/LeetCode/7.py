class Solution:
    def reverse(self, x: int) -> int:
        num = x
        res = 0
        
        if(x<0):
            x *= -1
        
        while(x>0):
            rem = x % 10
            res = (res * 10) + rem
            x = x // 10
        if(res > (2 ** 31)-1):
            return 0
        if(num<0):
            return res*-1
        else:
            return res