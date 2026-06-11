class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0 
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] += 1

            digits[i] += carry
            carry = 0

            if digits[i] > 9:
                carry = 1
                digits[i] = 0
        
        if carry == 1:
            digits.insert(0, 1)
        
        return digits