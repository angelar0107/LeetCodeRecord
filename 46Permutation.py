class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False for _ in nums]
        res = []
        self.helper(nums,used,res,[])
        return res
        
    def helper(self, nums, used, res, curr):
        if len(curr) == len(nums):
            res.append(list(curr))
        for i in range(len(nums)):
            if used[i] == False:
                used[i] = True
                curr.append(nums[i])
                self.helper(nums,used,res,curr)
                used[i] = False
                curr.pop()
