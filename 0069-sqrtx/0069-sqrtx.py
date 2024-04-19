class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x<4:
            return 1
        val=2
        while x//(val*val)>=1:
            val+=1
        return val-1