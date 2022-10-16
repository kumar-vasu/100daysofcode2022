class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        if len(jobDifficulty) < d: 
            return -1
        elif len(jobDifficulty) == d: 
            return sum(jobDifficulty)
        
        dp = [[float('inf')] * (len(jobDifficulty)) for _ in range(d)]
        
        dp[0][0] = jobDifficulty[0]
        
        for i in range(1, len(jobDifficulty)):
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i])
            
        for i in range(1, d):
            for j in range(i, len(jobDifficulty)):
                minDiff = 0
                for k in range(j, i-1, -1):
                    minDiff = max(minDiff, jobDifficulty[k])
                    dp[i][j] = min(dp[i][j], dp[i-1][k-1] + minDiff)
                    
        return dp[-1][-1]