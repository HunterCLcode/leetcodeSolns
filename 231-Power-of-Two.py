class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        cur = 1
        while cur < n:
            cur *= 2
        return cur == n
