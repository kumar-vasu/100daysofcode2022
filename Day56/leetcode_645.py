class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check = set(range(1,len(nums)+1))
        
        res = []
        
        for i in nums:
            if i in check:
                check.remove(i)
                
            else:
                res.append(i) 
        
        res.extend(list(check))
        return res