class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if k == 0 or len(prices) <= 1:
            return 0
        
        if 2*k > len(prices):
            res = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
                    
        
        
        dp = [-sys.maxsize if i%2 == 0 else 0 for i in range((2*k)+1)]
        
        dp[0] = -prices[0]
        
        for i in range(len(prices)):
            
            for j in range(len(dp)):
                
                if j == 0:
                    dp[j] = max(dp[j], -prices[i])
                    
                elif j%2 == 0:
                    dp[j] = max(dp[j], dp[j-1]-prices[i])
                    
                elif j%2 == 1:
                    dp[j] = max(dp[j], dp[j-1]+prices[i])
                    
        return dp[-2]