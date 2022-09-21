class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf') for i in range(n)]
        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices[:]
            
            for f, t, newPrice in flights:
                if prices[f] == float('inf'): continue
                tempPrices[t] = min(tempPrices[t], prices[f] + newPrice)
            prices = tempPrices
            
        return prices[dst] if prices[dst] != float('inf') else -1
        
        
