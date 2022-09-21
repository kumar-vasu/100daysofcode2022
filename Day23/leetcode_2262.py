class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        curSum, cumSum = 1, 1
        hashmap = {s[0]: 0}
        for i in range(1, n):
            if s[i] not in hashmap:
                curSum += i + 1
            else:
                curSum += i - hashmap[s[i]]
            cumSum += curSum
            hashmap[s[i]] = i
        return cumSum