class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size=len(matrix)
        for i in range(round(size/2)):
            for j in range(i,size-i):
                if i!=j:
                    tmp = matrix[i][j]
                    matrix[i][j], matrix[j][size-i-1], matrix[size-i-1][size-j-1], matrix[size-j-1][i] \
                    = matrix[size-j-1][i], tmp, matrix[j][size-i-1], matrix[size-i-1][size-j-1]           
        return matrix

