class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #One-pass
        
        red, white, blue = 0, 0, len(nums)-1
    
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        
        #Two-pass
        
        zero, one = 0, 0
        for num in nums:
            if num == 0:
                zero += 1
            if num == 1:
                one += 1
        for i in range(len(nums)):
            if i + 1 <= zero:
                nums[i] = 0
            elif i + 1 <= zero + one:
                nums[i] = 1
            else:
                nums[i] = 2
        
        
        
        
