class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [None]
        curr_left = nums[0]
        for i in range(1, len(nums)):
            left.append(curr_left)
            curr_left *= nums[i]
            
        right = [None]
        curr_right = nums[-1]
        for i in range(1, len(nums)):
            right = [curr_right] + right
            curr_right *= nums[len(nums) - i - 1]
            
        res = []
        for i in range(len(nums)):
            curr = 1
            if left[i] != None:
                curr *= left[i]
            if right[i] != None:
                curr *= right[i]
            res.append(curr)
                
        return res
            