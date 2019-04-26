class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l = [i for i in range(1,n + 1)]
        result = []
        self.dfs(l,result,[],k)
        return result
        
        
        
    def dfs(self, l, result, curr, k):
        if k == 0:
            result.append(curr)
            return
        if not l:
            return
        for i in range(len(l)):
            self.dfs(l[i + 1:],result, curr + [l[i]], k - 1)
        
