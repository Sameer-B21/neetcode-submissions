class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = prices[0]
        for i in range(len(prices)):
            if prices[i]<l:
                l = prices[i]
            elif prices[i]>l and prices[i]-l > p:
                p = prices[i]-l
        return p



        