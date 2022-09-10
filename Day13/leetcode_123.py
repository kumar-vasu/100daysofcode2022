class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = [0 for i in range(len(prices))]
        
        right = [0 for i in range(len(prices))]
        
        lmin = prices[0]
        for i in range(1, len(prices)):
            left[i] = max(left[i-1], prices[i] - lmin)
            
            lmin = min(prices[i], lmin)
            
        rmax = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            
            right[i] = max(right[i+1], rmax - prices[i])
            
            rmax = max(prices[i], rmax)
            
        profit = [0 for i in range(len(prices))]
        
        max_profit = 0
        for i in range(len(prices)):
            profit[i] = max(max_profit, left[i] + right[i])
            
            max_profit = max(profit[i], max_profit)
        
        print(left, right, profit)
        return max_profit
            