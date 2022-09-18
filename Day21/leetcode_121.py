class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_ = prices[0]
        min_ = prices[0]
        res = -sys.maxsize
        for i in range(1, len(prices)):
            if prices[i] <= min_:
                min_ = prices[i]
                max_ = prices[i]
            else:
                max_ = prices[i]
                res = max(res, max_ - min_)
                
        if res == -sys.maxsize:
            return 0
        return res