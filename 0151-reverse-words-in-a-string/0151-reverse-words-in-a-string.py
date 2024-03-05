class Solution:
    def reverseWords(self, s: str) -> str:
        list_words=s.split()
        print(list_words)
        list_reverse_words=[]
        lg=len(list_words)
        for i in range(lg-1, -1 , -1):
            list_reverse_words.append(list_words[i])
        return " ".join(list_reverse_words)