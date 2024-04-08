class Solution:
    def isValid(self, s: str) -> bool:
        left_char = []
        corres_dic={'(':')', '[':']', '{':'}'}
        if len(s)%2==1:
            return False
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                left_char.append(s[i])
            else: 
                if left_char==[]:
                    return False
                c_left=left_char.pop()
                if corres_dic[c_left]!=s[i]:
                    return False
        if left_char:
            return False
        return True
            
            

        