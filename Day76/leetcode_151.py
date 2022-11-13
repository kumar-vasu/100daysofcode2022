import re

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(reversed(re.sub("  +", " ", s.strip()).split(" "))))