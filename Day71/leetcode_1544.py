class Solution:
    def makeGood(self, s: str) -> str:
        left = 0
        right = 1
        while right < len(s):
            if (s[left] == s[right].lower() or s[left].lower() == s[right]) and s[left] != s[right]:
                s = s[:left]+s[right+1:]
                left = 0
                right = 1
            else:
                left += 1
                right += 1
        return s
