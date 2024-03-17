class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nb_level=len(triangle)
        if nb_level==0:
            return 0
        if nb_level==1:
            return min(triangle[0])
        nb_each_level=[x+1 for x in range(nb_level)]
        dp=[[0]*nb for nb in nb_each_level]
        dp[0][0]=triangle[0][0]
        for i in range(1,nb_level):
            for j in range(nb_each_level[i]):
                #print(i,j,dp)
                if j!=0 and j!=nb_each_level[i]-1:
                    #print("middle")
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
                elif j==0:
                    #print("here",dp[i-1][j],triangle[i][j])
                    dp[i][j]=dp[i-1][j]+triangle[i][j]
                else:
                    #print("there",dp[i-1][j-1],triangle[i][j])
                    dp[i][j]=dp[i-1][j-1]+triangle[i][j]
        return min(dp[nb_level-1])
                    