class Solution:
    def trailingZeroes(self, n: int) -> int:
        cpt=0
        sum_val=1
        for i in range(1,n+1):
            sum_val*=i
        while sum_val%10==0:
            sum_val=sum_val//10
            cpt+=1
        return cpt