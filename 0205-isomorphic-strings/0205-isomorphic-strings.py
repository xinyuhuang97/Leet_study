class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cpt=97
        dic_s={}
        dic_t={}
        new_str_s, new_str_t='', ''
        for c in s:
            if c not in dic_s:
                dic_s[c]=chr(cpt)
                new_str_s+=chr(cpt)
                cpt+=1
            else:
                new_str_s+=dic_s[c]
        cpt=97
        for c in t:
            if c not in dic_t:
                dic_t[c]=chr(cpt)
                new_str_t+=chr(cpt)
                cpt+=1
            else:
                new_str_t+=dic_t[c]
        print(new_str_t, new_str_s)
        return new_str_s==new_str_t
        
            
            