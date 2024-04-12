class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s=s.split(' ')
        if len(s)!=len(pattern):
            return False
        dic_pattern={}
        dic_s={}
        new_s=''
        for i in range(len(pattern)):
            if s[i] not in dic_pattern:
                if pattern[i]  in dic_s:
                    return False
                dic_s[pattern[i]]=s[i]
                dic_pattern[s[i]]=pattern[i]
                new_s+=pattern[i]
            else:
                new_s+=dic_pattern[s[i]]
        print(new_s, pattern)
        return new_s==pattern