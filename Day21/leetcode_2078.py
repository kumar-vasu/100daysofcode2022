class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_ = -sys.maxsize
        
        for i in range(1, len(colors)):
            for j in range(i):
                if colors[i] != colors[j]:
                    max_ = max(max_, i-j)
                    
        return max_