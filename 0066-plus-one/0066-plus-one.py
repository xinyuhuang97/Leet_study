class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lg=len(digits)
        for i in range(lg):
            if i==lg-1:
                plus_one=digits[lg-1]+1
                if plus_one==10:
                    bool_plus_one=True
                    j=i
                    while bool_plus_one:
                        print(j,digits)
                        digits[j]=0
                        if j-1==0:
                            digits[0]+=1
                            if digits[0]==10:
                                digits[0]=0
                                digits=[1]+digits
                            break
                        elif j-1<0:
                            digits=[1]+digits
                            break
                        else:
                            digits[j-1]=digits[j-1]+1
                            if digits[j-1]!=10:
                                bool_plus_one=False
                            j-=1
                else:
                    digits[lg-1]=digits[lg-1]+1
        return digits
                                
                    