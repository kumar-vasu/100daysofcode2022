class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1:
            curr = [i for i in str(n)]
            sum_sq = 0
            for i in curr:
                sum_sq += int(i)**2
            n = sum_sq
            if n in seen:
                return False
            else:
                seen.add(n)
        if n == 1:
            return True