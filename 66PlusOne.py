class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            temp = digits[i] + carry
            digits[i],carry = temp % 10, temp // 10
            if not carry:
                return digits
        if carry == 1:
            return [1] + digits
        return digits
