class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if len(nums) <= 1:
            if len(nums) == 1 and nums[0] == val:
                return 0
            else:
                return len(nums)
        
        additions = 0
        i = 0
        counter = 0
        while counter < len(nums):
            #print(i, nums)
            curr = nums[i]
            if curr == val:
                nums.pop(i)
                nums.append("_")
                additions += 1
            else:
                i += 1
            counter += 1
                
        return len(nums) - additions