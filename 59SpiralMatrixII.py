class Solution:
    def generateMatrix(self, n):
        if n < 1:
            return []
        result = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        left, right, up, down = 0, n - 1, 0,n - 1
        while num <= n**2:
            # if r:
            for i in range(left,right + 1):
                result[up][i] = num
                num += 1
            up += 1
            for i in range(up,down + 1):
                result[i][right] = num
                num += 1
            right -= 1
            for i in range(right, left - 1, -1):
                result[down][i] = num
                num += 1
            down -= 1
            for i in range(down, up - 1, -1):
                result[i][left] = num
                num += 1
            left += 1
        return result

        
        
