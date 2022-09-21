class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums1) + 1)] for j in range(len(nums2) + 1)]

        max_len = 0

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    continue

                if nums2[i-1] == nums1[j-1]:
                    dp[i][j] = dp[i -1][j -1] + 1
                    max_len = max(max_len, dp[i][j])

        return max_len