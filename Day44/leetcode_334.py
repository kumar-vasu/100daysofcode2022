class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        check = False
        small = sys.maxsize
        large = sys.maxsize
        for i in nums:
            if i <= small:
                small = i
            elif i <= large:
                large = i
            else:
                check = True
                break
        return check    
        