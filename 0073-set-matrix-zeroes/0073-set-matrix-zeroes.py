class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        zero_col=[]
        zero_line=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zero_col.append(i)
                    zero_line.append(j)
        for i in zero_col:
            for j in range(n):
                matrix[i][j]=0
        for i in range(m):
            for j in zero_line:
                matrix[i][j]=0
        