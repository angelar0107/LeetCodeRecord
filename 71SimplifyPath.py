class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist = path.split('/')
        result = []
        for i in range(len(pathlist)):
            curr = pathlist[i]
            if curr == '.' or not curr:
                continue
            elif curr == '..':
                if result:
                    result.pop()
                continue
            result.append(curr)
        return '/' + '/'.join(result)
            
        
