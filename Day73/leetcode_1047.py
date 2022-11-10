class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for x in s:
            if len(res) > 0 and res[-1] == x:
                res.pop()
            else:
                res.append(x)
        return ''.join(res)
