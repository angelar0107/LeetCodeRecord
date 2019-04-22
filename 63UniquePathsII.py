class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if not obstacleGrid or not m:
            return 0
        n = len(obstacleGrid[0])
        dp = [[1 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0]:
            dp[0][0] = 0
        for i in range(1,n):
            if not dp[0][i-1] or obstacleGrid[0][i]:
                dp[0][i] = 0
        for j in range(1,m):
            if not dp[j-1][0] or obstacleGrid[j][0]:
                dp[j][0] = 0
                
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp [i][j-1]
        return dp[-1][-1]
