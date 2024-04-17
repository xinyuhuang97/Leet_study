class Solution:
    def bi_to_dec(self, value):
        lg=len(value)
        result=0
        for bit in value:
            result+=int(bit)*2**(lg-1)
            lg-=1
        return result
    def addBinary(self, a: str, b: str) -> str:
        if a=="0" and b =="0":
            return a
        sum_decimal = self.bi_to_dec(a) + self.bi_to_dec(b)
        s=''
        print(sum_decimal)
        while sum_decimal:
            s+=str(sum_decimal%2)
            sum_decimal=sum_decimal//2
        return s[::-1]
            