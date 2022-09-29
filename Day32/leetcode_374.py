# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        left = 0
        right = n
        
        while left <= right:
            mid = (left + right)//2
            
            pick = guess(mid)
            if pick == 0:
                return mid
            
            elif pick == -1:
                right = mid - 1
                continue
                
            else:
                left = mid + 1
                continue
                
        return