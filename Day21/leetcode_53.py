class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = float('-inf')
        curr = 0
        
        for i in range(len(nums)):
            if curr < 0:
                curr = nums[i]
            else:
                curr += nums[i]
            max_sum = max(max_sum, curr)
            
        return max_sum
                