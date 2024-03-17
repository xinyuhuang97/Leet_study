class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        size_r, size_c=len(grid),len(grid[0])
        dp=[[0]*size_c for _ in range(size_r)]
        dp[0][0]=grid[0][0]
        
        for i in range(size_r):
            for j in range(size_c):
                if i==0 and j==0:
                    continue
                if i==0: 
                    dp[i][j]=dp[0][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j]=dp[i-1][0]+grid[i][j]
                else:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j])+grid[i][j]
        print(dp)
        return dp[size_r-1][size_c-1]
                    