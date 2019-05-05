class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if not s3:
            return False
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len1 + len2 != len3:
            return False
        dp = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        dp[0][0] = True
        for i in range(len1):
            dp[i + 1][0] = s1[i] == s3[i] and dp[i][0]
        for j in range(len2):
            dp[0][j + 1] = s2[j] == s3[j] and dp[0][j]
      
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
                if s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        return dp[-1][-1]
                
