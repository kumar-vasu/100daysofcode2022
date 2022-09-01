class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        dp = {}
        
        def recurse(nums, x, left, right, count):
            
            if x == 0:
                return count
                        
            if left > right or x < 0:
                return sys.maxsize
            
            if (left, right, x) in dp:
                return dp[(left, right, x)]

            
            l = recurse(nums, x - nums[left], left+1, right, count+1)
            
            r = recurse(nums, x - nums[right], left, right-1, count+1)
            
            dp[(left, right, x)] = min(l, r)
            
            return dp[(left, right, x)]
        
        result = recurse( nums, x, 0, len(nums)-1, 0)
        if result == sys.maxsize:
            return -1
        return result