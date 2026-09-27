class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        j = len(matrix) - 1
        #reverse the rows: 
        for i in range(len(matrix) // 2): 
            temp = matrix[i]
            matrix[i] = matrix[j]
            matrix[j] = temp
            j -= 1
        for i in range(len(matrix)): 
            for j in range(i+1, len(matrix)): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
