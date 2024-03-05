class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lg=len(strs)
        if lg==0 or strs[0]=="" :
            return ""
        prefix=""
        first_word=strs[0]
        lg_fw=len(first_word)
        for i in range(lg_fw):
            letter = first_word[i]
            for word in strs[1:]:
                try:
                    letter_word=word[i]
                except:
                    return prefix
                if letter_word!=letter:
                        if i==0:
                            return ""
                        else:
                            return prefix
            prefix+=letter
        return prefix