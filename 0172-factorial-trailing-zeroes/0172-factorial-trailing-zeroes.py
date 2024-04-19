class Solution:
    def trailingZeroes(self, n: int) -> int:
        cpt=0
        value=5
        while n//value>=1:
            cpt+=n//value
            value*=5
        return cpt