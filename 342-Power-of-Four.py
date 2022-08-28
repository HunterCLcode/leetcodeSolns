class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cur = 1
        
        while True:

            if cur == n:
                return True
            elif cur > n:
                return False
            cur *= 4
