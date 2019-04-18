class Solution:
    def canJump(self, nums: List[int]) -> bool:
        able = nums[0]
        for i in range(len(nums)):
            if i > able:
                return False
            able = max(nums[i] + i,able)
        return True
