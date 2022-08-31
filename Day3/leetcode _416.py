class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0 :
            return False
        
        half_sum = sum(nums)//2
        
        dp = [[False if i!=0 else True for i in range(half_sum + 1)] for j in range(len(nums) + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0 or j==0:
                    continue
                    
                if nums[i-1] > j:
                    include = False
                else:
                    include = dp[i-1][j-nums[i-1]]
                
                exclude = dp[i-1][j]
                
                dp[i][j] = exclude or include
                
        return dp[-1][-1]