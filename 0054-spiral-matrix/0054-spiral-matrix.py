class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==1 :
            return matrix[0]
        if len(matrix[0])==1:
            return [x[0] for x in matrix]
        result = []
        step_horizontal, step_vertical = len(matrix[0]), len(matrix)-1
        x, y = 0, -1
        cpt=0
        while cpt<len(matrix[0])*len(matrix) :
            print()
            for i in range(step_horizontal):
                cpt+=1
                y  = y + 1
                result.append(matrix[x][y])
            if cpt == len(matrix[0])*len(matrix):
                return result
            step_horizontal-=1
            for i in range(step_vertical):
                cpt+=1
                x = x + 1
                result.append(matrix[x][y])
            if cpt == len(matrix[0])*len(matrix):
                return result
            step_vertical-=1
            for i in range(step_horizontal):
                cpt+=1
                y  = y - 1
                result.append(matrix[x][y])
            step_horizontal-=1
            for i in range(step_vertical):
                cpt+=1
                x = x - 1
                result.append(matrix[x][y]) 
            step_vertical-=1
        return result
     