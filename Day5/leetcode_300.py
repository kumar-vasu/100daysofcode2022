class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc_sub = [1]*len(nums)
        maximum = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc_sub[i] = max(inc_sub[i], inc_sub[j]+1)
                    maximum = max(inc_sub[i], maximum)
        return maximum