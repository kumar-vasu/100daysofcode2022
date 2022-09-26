class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        
        for i in range(len(nums)):
            if i%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
                
        odd = sorted(odd, reverse = True)
        even = sorted(even)
        
        res = []
        for i in range(len(nums)):
            if i%2 == 0:
                res.append(even.pop(0))
            else:
                res.append(odd.pop(0))
                
        return res