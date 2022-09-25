class Solution:
    def isPalindrome(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s) - i -1]:
                return False
        return True
    
    def firstPalindrome(self, words: List[str]) -> str:
        
        for i in words:
            if self.isPalindrome(i):
                return i
            
        return ""