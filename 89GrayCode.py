class Solution:
    def grayCode(self, n: int) -> List[int]:
        if not n:
            return [0]
        first = self.grayCode(n - 1)
        res = first
        for i in range(len(first) - 1, -1, -1):
            res.append(2**(n - 1) + first[i])
        return res
