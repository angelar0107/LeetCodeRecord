class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        self.mysum(1,k,n,[])
        return self.result
              
    def mysum(self,start,k,n,path):
        if n == 0 and k == 0:
            self.result.append(path)
            return
        if k == 0 or n <= 0:
            return
        for i in range(start,10):
            self.mysum(i+1,k-1,n-i,path+[i])
