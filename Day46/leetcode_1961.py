class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        test = ''
        for i in words:
            test += i
            if test == s:
                return True
        return False