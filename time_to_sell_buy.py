class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(1, len(prices)): #generate pointer via range to use as index
            if prices[r] < prices[l]: #from the second index. if the right is less than the left, then this is the lowest price. 
                l = r
            res = max(res, prices[r] - prices[l]) # compare the delta between the lowest price and the current pointier, right. 
        return res