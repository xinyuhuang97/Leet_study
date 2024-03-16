class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lg=len(s)
        if lg<=1:
            return lg
        l,list_c,current_s,ans=0,[],'',0
        for r,letter in enumerate(s):
            print(current_s, list_c)
            if letter not in list_c:
                
                current_s+=letter
                ans=max(ans,len(current_s))
                list_c.append(letter)
            else:
                while letter in list_c:
                    ans=max(ans,len(current_s))
                    list_c.remove(current_s[0])
                    current_s=current_s[1:]
                list_c.append(letter)
                current_s+=letter
        return ans
                    