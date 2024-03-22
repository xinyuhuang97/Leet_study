class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x=list(str(x))
        n=len(string_x)
        for i in range(n//2):
            if string_x[i]!=string_x[n-i-1]:
                return False
        return True