class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bit = bin(n)
        cpt=0
        for i in range(len(n_bit)):
            if n_bit[i]=='1':
                cpt+=1
        return cpt