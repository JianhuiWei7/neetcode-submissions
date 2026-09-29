class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits)):
            index = len(digits) - 1 - i
            digits[index] += carry
            if digits[index] < 10:
                return digits
            else:
                carry = digits[index] // 10
                digits[index] = digits[index] % 10
                
        if carry != 0:
            digits.insert(0, carry)
        return digits
        
        
