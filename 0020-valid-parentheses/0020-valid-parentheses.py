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
                if left_char==[] or corres_dic[left_char.pop()]!=s[i]:
                    return False
        return left_char==[]
            
            

        