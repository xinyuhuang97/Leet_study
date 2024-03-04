class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_word=s.split()
        return len(list_word[-1])
        