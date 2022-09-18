class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float('-inf')
        cur_prod = 1
        for i in nums:
            if cur_prod == 0:
                cur_prod = 1
            cur_prod *= i
            max_prod = max(max_prod,cur_prod)
        
        cur_prod = 1
        for i in reversed(nums):
            if cur_prod == 0:
                cur_prod = 1
            cur_prod *= i
            max_prod = max(max_prod,cur_prod)
        return max_prod