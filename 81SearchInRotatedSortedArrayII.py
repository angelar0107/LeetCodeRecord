class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = end - (end - start) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[start]:
                if nums[mid] < target or nums[start] > target:
                    start = mid
                else:
                    end = mid
            if nums[mid] < nums[start]:
                if nums[mid] > target or nums[end] < target:
                    end = mid
                else:
                    start = mid
            else:
                for i in range(start, end + 1):
                    if nums[i] == target:
                        return True
                return False
        if nums[start] == target or nums[end] == target:
            return True
        return False
                    
        
