class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_column_has_zero = False

        for i in range(rows):
            if matrix[i][0] == 0 :
                first_column_has_zero = True
        for j in range(cols):
            if matrix[0][j] == 0 :
                first_row_has_zero = True
        
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0                   
        
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_column_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
