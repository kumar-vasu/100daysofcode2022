class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def palindrome(s):
            if s == s[::-1]:
                return True
            return False
        
        if palindrome(s):
            return True
        
        left = 0
        right = len(s) - 1
        
        while left <= right:
            if s[left] != s[right]:
                
                temp1 = s[:right] + s[right + 1:]
                temp2 = s[:left] + s[left + 1 :]
                if palindrome(temp1) or palindrome(temp2):
                    return True
                else:
                    return False
            else:
                left += 1
                right -= 1
        