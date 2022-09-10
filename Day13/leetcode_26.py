class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return len(nums)
        
        prev = nums[0]
        curr = None
        additions = 0
        i = 1
        counter = 1
        while counter < len(nums):
            #print(i, nums)
            curr = nums[i]
            if curr == prev:
                nums.pop(i)
                nums.append("_")
                additions += 1
            else:
                prev = curr
                i += 1
            counter += 1
                
        return len(nums) - additions
                