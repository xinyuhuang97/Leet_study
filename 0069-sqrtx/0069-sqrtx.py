class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x<4:
            return 1
        xn=x
        while xn**2 > x:
            xn = (xn+x//xn)//2
        return xn