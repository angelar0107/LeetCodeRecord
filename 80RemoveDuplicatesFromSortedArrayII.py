class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        fast, slow = 1, 1
        while fast < len(nums):
            nums[slow] = nums[fast]
            if nums[slow] != nums[slow - 1]:
                count = 1
            else:
                count += 1
            if count <= 2:
                slow += 1
            fast += 1
        return slow
    
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        while length < len(nums):
            if length < 2 or nums[length] != nums[length - 2]:
                length += 1
            else:
                nums.pop(length)
        return length
            
            
            
        
