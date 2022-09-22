class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 1
        temp = 1
        for i in range(1,n+1):
            ans = 9*temp + ans
            temp = temp*(10-i)

        return ans