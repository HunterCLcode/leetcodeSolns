class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [float('inf') if i != 0 else 0 for i in range(amount + 1)]

        for i in range(amount + 1):
            for coin in coins:
                current = i - coin
                if current > -1:
                    cache[i] = min(cache[i], cache[current] + 1)
        
        return cache[-1] if cache[-1] != float('inf') else -1
