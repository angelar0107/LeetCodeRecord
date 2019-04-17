from heapq import heapify,heappop,heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapify(heap)
        for i in nums:
            if len(heap) < k:
                heappush(heap,i)
            else:
                temp = max(heappop(heap),i)
                heappush(heap,temp)
        return heappop(heap)
