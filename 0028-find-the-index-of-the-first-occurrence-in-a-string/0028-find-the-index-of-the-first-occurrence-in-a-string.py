class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack==needle:
            return 0
        lg_n=len(needle)
        lg_h=len(haystack)
        index=0
        while index+lg_n<=lg_h:
            if haystack[index:index+lg_n]==needle:
                return index
            index+=1
        return -1