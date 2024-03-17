class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nb_level=len(triangle)
        if nb_level==0:
            return 0
        if nb_level==1:
            return min(triangle[0])
        dp=[[0]*(nb+1) for nb in range(nb_level)]
        dp[0][0]=triangle[0][0]
        for i in range(1,nb_level):
            for j in range(i+1):
                if j!=0 and j!=len(triangle[i])-1:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
                elif j==0:
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                else:
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
        return min(dp[nb_level-1])
                    