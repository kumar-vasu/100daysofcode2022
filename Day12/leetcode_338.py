class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0 for _ in range(n+1)]
        
        for i in range(1, len(result)):
            if i%2 == 0:
                result[i] = result[i//2]
            else:
                result[i] = result[i//2] + 1
                
        return result