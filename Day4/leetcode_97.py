class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        dp = {}
        
        def recurse(s1p, s1, s2p, s2, s3p, s3):
            
            if s1p == len(s1):
                return True
            elif s2p == len(s2) and s3p == len(s3):
                return False
            
            if (s1p, s2p, s3p) in dp:
                return dp[(s1p, s2p, s3p)]
            
            if s3p < len(s3):
                if s3[s3p] == s1[s1p]:
                    include3 = recurse(s1p+1, s1, s2p, s2, s3p+1, s3)
                else:
                    include3 = False
            if s2p < len(s2):
                if s2[s2p] == s1[s1p]:
                    include2 = recurse(s1p+1, s1, s2p+1, s2, s3p, s3)
                else:
                    include2 = False
            print((s1p, s2p, s3p), include2, include3)
            dp[(s1p, s2p, s3p)] = include3 or include2
            return dp[(s1p, s2p, s3p)]
        
        result = recurse
        
        return result