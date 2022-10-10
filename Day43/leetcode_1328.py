import copy

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        prev = copy.deepcopy(palindrome)
        
        for i in range(len(palindrome)):
            curr = palindrome[i]
            if ord(curr) > ord('a'):
                if len(palindrome) % 2 == 1 and i == len(palindrome)// 2:
                    continue
                elif i < len(palindrome)-1:
                    palindrome = palindrome[:i] + 'a' + palindrome[i+1:]
                else:
                    palindrome = palindrome[:i] + 'a'
                break
                
        if prev == palindrome:
            return palindrome[:-1] + chr(ord(palindrome[-1]) + 1)
        else:
            return palindrome