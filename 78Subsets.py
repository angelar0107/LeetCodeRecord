class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.dfs(nums,[],result)
        return result
         
    def dfs(self,nums,curr,result):
        result.append(curr)
        for i in range(len(nums)):
            self.dfs(nums[i+1:],curr + [nums[i]],result)
            
