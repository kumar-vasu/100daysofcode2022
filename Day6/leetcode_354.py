class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        LIS = [1 for i in range(len(envelopes))]
        
        envelopes = [i for i in reversed(sorted(envelopes))]
        
        maxl = 1
        
        for i in range(1, len(LIS)):
            for j in range(i):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1] and LIS[j] + 1 > LIS[i]:
                    LIS[i] = LIS[j] + 1
                    maxl = max(maxl, LIS[i])
                    
        return maxl
                    
                    