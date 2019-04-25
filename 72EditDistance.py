class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n,m = len(word1) + 1, len(word2) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = i
        for j in range(1, n):
            dp[0][j] = j
        for i in range(1, m):
            for j in range(1, n):
                if word1[j - 1] == word2[i - 1]:
                    dif = 0
                else:
                    dif = 1
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j -1] + 1, dif + dp[i - 1][j - 1])
        return dp[-1][-1]
