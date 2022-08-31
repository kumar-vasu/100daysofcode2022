class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, nums):
        total = sum(nums)
        
        half_sum = total//2
        
        dp = [[True if i== 0 else False for i in range(half_sum + 1)] for j in range(len(nums) + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i ==0  or j==0:
                    continue
                    
                exclude = dp[i-1][j]
                
                if nums[i-1] > j:
                    include = False
                else:
                    include = dp[i-1][j-nums[i-1]]
                
                dp[i][j] = exclude or include
        
        result = 0
        for j in range(len(dp[0])):
            if dp[-1][j] == True:
                result = j
                
        return abs(total - 2*result)