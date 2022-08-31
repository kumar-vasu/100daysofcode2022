class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        dp = [[sys.maxsize if i != 0 else 0 for i in range(amount + 1)] for j in range(len(coins) + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    continue
                    
                exclude = dp[i-1][j]
                
                if coins[i-1] > j:
                    include = sys.maxsize
                else:
                    include = dp[i][j - coins[i-1]] + 1
                    
                dp[i][j] = min(include, exclude)
        
        if dp[-1][-1] == sys.maxsize:
            return -1
        else:
            return dp[-1][-1]