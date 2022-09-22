class Solution:
    def reverseWords(self, s: str) -> str:
        res = ["".join(list(reversed(i))) for i in s.split(" ")]
        res = " ".join(res)
        return res