import copy
class Solution:
    def findComplement(self, num: int) -> int:
        
        num_copy = copy.deepcopy(num)
        p = 1
        
        while num_copy > 1:
            num_copy >>= 1
            p <<= 1
            p |= 1
        print(p)
        print(num)
            
        return num ^ p