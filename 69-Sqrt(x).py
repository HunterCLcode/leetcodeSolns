class Solution:
    def mySqrt(self, x: int) -> int:
        # Try to get it so that left pointer is below sqrt and right pointer is above sqrt
        # Do this by getting midval, see if its above or below sqrt. If above, set to right
        # Else set to left. Do this until left is one below right and return left
        if x < 2:
            return x
        l, r = 0, x
        
        while r - l > 1:
            m = int((r - l) / 2) + l
            if m * m > x:
                r = m
            elif m * m < x:
                l = m
            else:
                return m
        return l
        
