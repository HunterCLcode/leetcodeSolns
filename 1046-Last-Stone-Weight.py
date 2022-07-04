class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            b, l = heapq.heappop(stones), heapq.heappop(stones)
            # Bang them together!
            if b < l:
                heapq.heappush(stones, b - l)
        return -1 * stones[0] if stones else 0