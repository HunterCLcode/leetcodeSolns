class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, output = 0, 0
        for r in range(1,len(prices)):
            output = max(prices[r] - prices[l], output)
            if prices[r] < prices[l]: l = r
        return output
