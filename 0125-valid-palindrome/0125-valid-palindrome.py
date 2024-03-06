class Solution:
    def isPalindrome(self, s: str) -> bool:
        #"A" - "Z" varie de 65 à 90 et celle de "a" - "z" de 97 à 122.
        lg=len(s)
        if lg==1:
            return True
        s=s.replace(" ","")      
        list_s="".join(i.lower() for i in s if i.isalnum())
        lg=len(list_s)
        lg_half=int(lg/2)
        for i in range(lg_half):
            if list_s[i]!=list_s[lg-i-1]:
                return False
        return True
        