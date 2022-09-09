class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        
        for i in nums:
            xor ^= i
        
        p = 1
        while (xor&1 == 0):
            xor >>= 1
            p <<= 1
        
        p1 = 0
        p2 = 0
        
        for i in nums:
            if i & p == p:
                p1 ^= i
            else:
                p2 ^= i
                
        return [p1, p2]