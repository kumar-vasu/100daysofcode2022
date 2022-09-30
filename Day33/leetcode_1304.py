class Solution:
    def sumZero(self, n: int) -> List[int]:
        even = False
        if n % 2 == 0:
            even = True
        res = []
        if not even:
            res.append(0)
            
        for i in range(1, n):
            if len(res) == n:
                break
            res.append(i)
            res.append(-i)
                
        return res
            