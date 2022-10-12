class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = -2
        for i in range(1, len(nums)):
            for j in range(i):
                prod = max(prod, (nums[i]-1)*(nums[j]-1))
        return prod