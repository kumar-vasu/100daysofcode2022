class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def helper(s, cur, last, count, k, dp):
            if k < 0:
                return float('inf')
            if cur >= len(s):
                return 0

            if (cur, last, count, k) in dp:
                return dp[(cur, last, count, k)]

            result = float('inf')
            result = helper(s, cur + 1, last, count, k - 1, dp)
            if s[cur] != last:
                result = min(result, 1 + helper(s, cur + 1, s[cur], 1, k, dp))
            else:
                if count == 1 or count == 9 or count == 99:
                    result = min(result, 1 + helper(s, cur + 1, last, count + 1, k, dp))
                else:
                    result = min(result, helper(s, cur + 1, last, count + 1, k, dp))

            dp[(cur, last, count, k)] = result
            return result

        return helper(s, 0, '#', 0, k, {})