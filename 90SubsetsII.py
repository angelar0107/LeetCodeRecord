class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        use = [False for _ in range(len(nums))]
        result = []
        self.dfs(nums,use,result,[],0)
        return result
        
        
    def dfs(self,nums,use,result,curr,index):
        result.append(curr)
        for i in range(index,len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not use[i - 1]:
                continue
            use[i] = True
            self.dfs(nums,use,result,curr + [nums[i]], i + 1)
            use[i] = False


#Leetcode Template Ver.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False for _ in nums]
        self.dfs(nums,res,used,0,[])
        return res
    
    def dfs(self,nums,res,used,index,curr):
        res.append(list(curr))
        for i in range(index,len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                continue
            curr.append(nums[i])
            used[i] = True
            self.dfs(nums,res,used,i + 1, curr)
            curr.pop()
            used[i] = False
            
                
