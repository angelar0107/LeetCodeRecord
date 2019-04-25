class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Time Complexity is O((mn)(m+n)) 
        #Space Complexity is O(1)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = '#'
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = '#'
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = '#'
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0
        
    def setZeroes(self,matrix):
        #Time Complexity is O(mn)
        #Space Complexity is O(m + n)
        
        m, n = len(matrix),len(matrix[0])
        row, column  = [1] * m, [1] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = column[j] = 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] *= row[i]*column[j]
                    
    
