class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        
        res = s
        for i in range(len(s)):
            
            s = s[1:] + s[0]
            res = min(s, res)
            
        return res