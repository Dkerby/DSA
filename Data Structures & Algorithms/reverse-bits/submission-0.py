class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        i = 0
        while n > 0:
            if n & 1 == 1:
                result = result | (1 << (31 - i))
            
            n = n >> 1
            i += 1
        
        return result