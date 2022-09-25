class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        for i in range(len(s)//2):
            if s[i] in vowels:
                count += 1
            if s[len(s) - i - 1] in vowels:
                count -= 1
        
        if count == 0:
            return True
        else:
            return False