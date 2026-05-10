class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        for b_p in range(len(prices) - 1):
            for c_p in range(b_p+1,len(prices)):
                if prices[b_p] > prices[c_p]:
                    continue
                profit = prices[c_p] - prices[b_p]
                max_profit = max(max_profit,profit)
        return max_profit