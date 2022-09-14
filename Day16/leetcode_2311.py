class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res, cur = s.count("0"), 0

        for i, ch in enumerate(s[::-1][:30]):
            if ch == "1":
                cur |= 1 << i
                if cur > k:
                    return res
                res += 1

        return res