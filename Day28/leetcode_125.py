class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        s = "".join([s[i] if (ord(s[i]) >= 97 and ord(s[i]) <= 122)or(ord(s[i]) >= 48 and ord(s[i]) <= 57) else "" for i in range(len(s))])
        
        print(s)
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True