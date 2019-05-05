class Solution:
    
    
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2,n + 1):
            for j in range(1,i + 1):
                left = dp[j - 1]
                right = dp[i - j]
                dp[i] += left * right
        return dp[-1]
    
    
    def numTrees(self, n: int) -> int:
        cache = ['*' for _ in range(n + 1)]
        return self.helper(cache,n)
           
    def helper(self, cache, n):
        if n == 0 or n == 1:
            return 1
        if cache[n] != '*':
            return cache[n]
        res = 0
        for i in range(1,n + 1):
            left = self.helper(cache, i - 1)
            right = self.helper(cache, n - i)
            res += left * right
        cache[n] = res
        return res
                
    
    
    
