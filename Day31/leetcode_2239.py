class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = sys.maxsize

        for num in nums:
            if abs(num - 0) < abs(res-0):
                res = num
            elif abs(num - 0) == abs(res-0):
                res = max(res, num)
        return res