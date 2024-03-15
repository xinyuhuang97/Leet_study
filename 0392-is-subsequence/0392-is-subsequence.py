class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lg_s=len(s)
        lg_t=len(t)
        if lg_s==0:
            return True
        if lg_t<lg_s:
            return False
        head_s=0
        head_t=0
        while head_t<lg_t:
            if s[head_s]==t[head_t]:
                head_s+=1
                if head_s==lg_s:
                    return True
            head_t+=1
        return False
            