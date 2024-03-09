class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lg=len(s)
        dp=[False]*(lg+1)
        dp[0]=True
        max_len=max([len(word) for word in wordDict])
        print(max_len)
        for i in range(1,lg+1):
            for j in range(i-1,  max(i-max_len-1, -1), -1):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i]=True
                    break
        return dp[lg]
    