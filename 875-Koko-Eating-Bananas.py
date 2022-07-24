class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        
        while l + 1 < r:
            m = (l + r)//2
            
            # Check if koko finishes with m bananas per hr
            time = 0
            for pile in piles:
                time += math.ceil(pile / m)
            
            if time <= h:
                r = m
            else:
                l = m
                
        return r
