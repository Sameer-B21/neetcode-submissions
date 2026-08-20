class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = prices[0]
        for price in prices:
            l = min(price, l)
            p = max(price - l, p)
        return p



        