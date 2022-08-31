class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        if amount == 0:
            return 1
        
        dp = [[0 if i != 0 else 1 for i in range(amount + 1)] for j in range(len(coins) + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    continue
                    
                exclude = dp[i-1][j]
                
                if coins[i-1] > j:
                    include = 0
                else:
                    include = dp[i][j - coins[i-1]]
                    
                dp[i][j] = include + exclude
        
        return dp[-1][-1]