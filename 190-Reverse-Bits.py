class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(0,32):
            output = output * 2 + n % 2
            n = n >> 1
        return output
            
            
