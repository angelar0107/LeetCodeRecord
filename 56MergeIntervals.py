
class Solution:
    def merge(self, intervals):
        result = []
        intervals.sort()  
        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(interval[1],result[-1][1])
            else:
                result.append(interval)
        return result
