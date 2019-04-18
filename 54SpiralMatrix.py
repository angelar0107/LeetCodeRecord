class Solution:
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            matrix = self.rotateMatrix(matrix)
        return result
        
        
    def rotateMatrix(self,matrix):
        if not matrix:
            return
        newmatrix = []
        for i in range(len(matrix[0]) - 1, -1, -1):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            newmatrix.append(temp)
        return newmatrix
        
