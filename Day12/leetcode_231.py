import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        value = math.log2(n)
        result = math.floor(value) == math.ceil(value)
        
        return result