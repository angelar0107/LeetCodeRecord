from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Solution 1, sort, O(nlogn)
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
        
        #Solution 2, O(n) O(n) extra space;
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        for key in dic:
            if dic[key] >= 2:
                return True
        return False
        
        
        #Solution 3, O(n^2) O(1) extra space
        #TLE
        for i in range(0,len(nums) - 1):
            for j in range(i + 1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        
