class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sum_ = set()
        
        for i in range(1, len(nums)):
            curr = nums[i] + nums[i-1]
            if curr in sum_:
                return True
            else:
                sum_.add(curr)
        return False