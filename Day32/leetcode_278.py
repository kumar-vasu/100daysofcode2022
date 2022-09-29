# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        
        while left <= right:
            mid = (left + right)//2
            
            pick = isBadVersion(mid)
            pick_L = isBadVersion(mid -1)
            
            if pick and not pick_L:
                return mid
            
            if not pick:
                left = mid + 1
                continue
            
            else:
                right = mid - 1
                continue
        return