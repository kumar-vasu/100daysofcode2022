class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        zeroes = 0
        for i in nums:
            if i == 0:
                zeroes += 1
                
        total = sum(nums)
        
        # target = total - 2neg
        # neg = (total - target)//2
        if target > total:
            return 0
        
        if (total - target)%2 != 0:
            return 0
        
        neg = (total - target)//2
        
        dp = [[0 if i!=0 else 1 for i in range(neg + 1)] for j in range(len(nums)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    continue
                if nums[i-1] > j or nums[i-1] == 0:
                    include = 0
                else:
                    include = dp[i-1][j-nums[i-1]]
                    
                exclude = dp[i-1][j]
                
                dp[i][j] = include + exclude
        
        return dp[-1][-1] * 2**zeroes