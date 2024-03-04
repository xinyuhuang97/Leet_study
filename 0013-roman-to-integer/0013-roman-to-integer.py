class Solution:
    def romanToInt(self, s: str) -> int:
        dic={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        lg=len(s)
        if lg<=1:
            return dic[s[0]]
        c_before=dic[s[1]]
        c_after=0
        value=0        
        for i in range(lg-1):
            c_before=dic[s[i]]
            c_after=dic[s[i+1]]
            if c_before<c_after:
                value+=-c_before
            else:
                value+=c_before
            c_before=c_after
        value+=c_before
        return value
            