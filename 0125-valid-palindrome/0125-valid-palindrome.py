class Solution:
    def isPalindrome(self, s: str) -> bool:
        #"A" - "Z" varie de 65 à 90 et celle de "a" - "z" de 97 à 122.
        """s=s.replace(" ","")      
        s="".join(i.lower() for i in s if i.isalnum())
        lg=len(s)
        for i in range(int(lg/2)):
            if s[i]!=s[lg-i-1]:
                return False
        return True"""
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True
        