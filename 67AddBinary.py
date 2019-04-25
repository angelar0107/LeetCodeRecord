class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry = '', '0'
        la, lb =len(a),len(b)
        if la < lb:
            a = '0'*(lb - la) + a
        if lb < la:
            b = '0'*(la - lb) + b
        for i in range(len(a) - 1, -1, -1):
            res,carry = self.addString(a[i],b[i],carry)
            result = res + result

        if carry == '1':
            return '1' + result
        return result
        
    def addString(self,a,b,carry):
        count = 0
        res, car = '0','0'
        if a == '1':
            count += 1
        if b == '1':
            count += 1
        if carry == '1':
            count += 1
        if count & 1:
            res = '1'
        if count // 1:
            car = '1'
        return res,car
        
