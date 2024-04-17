class Solution:
    def reverseBits(self, n: int) -> int:
        #return int(bin(n)[2:].zfill(32)[::-1],2)
        result = 0
        print(n)
        for i in range(32):
            lsb = n&1
            result = result<<1
            result = result|lsb
            n = n>>1
        return result
        