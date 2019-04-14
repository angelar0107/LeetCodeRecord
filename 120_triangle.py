class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        rows = len(triangle)
        for row in range(1,rows):
            triangle[row][0] += triangle[row-1][0]
            triangle[row][-1] +=triangle[row-1][-1]
            for j in range(1,row):
                triangle[row][j] += min(triangle[row-1][j-1],triangle[row-1][j])
        return min(triangle[-1])
        
