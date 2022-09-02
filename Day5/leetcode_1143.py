class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                
                if i == 0  or j == 0:
                    continue
                
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[-1][-1]
                    
                