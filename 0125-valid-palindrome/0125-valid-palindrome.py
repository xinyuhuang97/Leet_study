class Solution:
    def isPalindrome(self, s: str) -> bool:
        #"A" - "Z" varie de 65 à 90 et celle de "a" - "z" de 97 à 122.
        s=s.replace(" ","")      
        s="".join(i.lower() for i in s if i.isalnum())
        lg=len(s)
        for i in range(int(lg/2)):
            if s[i]!=s[lg-i-1]:
                return False
        return True
        