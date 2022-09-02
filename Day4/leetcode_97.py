class Solution:
    def isInterleave(self, s3: str, s2: str, s1: str) -> bool:
        
        if len(s3) + len(s2) != len(s1):
            return False
        
        dp = {}
        
        def recurse(s1p, s1, s2p, s2, s3p, s3):
            
            if s1p == len(s1):
                if s2p == len(s2) and s3p == len(s3):
                    return True
                else:
                    return False
            
            if (s1p, s2p, s3p) in dp:
                return dp[(s1p, s2p, s3p)]
            
            if s3p == len(s3):
                if s2[s2p] == s1[s1p]:
                    return recurse(s1p+1, s1, s2p+1, s2, s3p, s3)
                else:
                    return False
            if s2p == len(s2):
                if s3[s3p] == s1[s1p]:
                    return recurse(s1p+1, s1, s2p, s2, s3p+1, s3)
                else:
                    return False

            include2 = False
            include3 = False

            if s2[s2p] == s1[s1p]:
                    include2 = recurse(s1p+1, s1, s2p+1, s2, s3p, s3)
            if s3[s3p] == s1[s1p]:
                    include3 = recurse(s1p+1, s1, s2p, s2, s3p+1, s3)

            dp[(s1p, s2p, s3p)] = include3 or include2
            return dp[(s1p, s2p, s3p)]
        
        result = recurse(0, s1, 0, s2, 0, s3)
        
        return result