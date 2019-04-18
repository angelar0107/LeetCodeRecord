class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        #two dp [0,n-1] [1,n]
        dp = [0 for _ in range(len(nums) - 1)]
        dp[0],dp[1] = nums[0],max(nums[1],nums[0])
        for i in range(2,len(dp)):
            dp[i] = max(nums[i] + dp[i-2],dp[i-1])
        answer = dp[-1]
        
        dp[0],dp[1] = nums[1],max(nums[2],nums[1])
        for i in range(2,len(dp)):
            dp[i] = max(nums[i + 1] + dp[i-2],dp[i-1])
        return max(answer,dp[-1])
