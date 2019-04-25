class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low + 1 < high:
            mid = (high - low) // 2 + low
            if mid * mid == x:
                return mid
            if mid * mid < x:
                low = mid
            else:
                high = mid
        if high * high > x:
            return low
        return high
        
