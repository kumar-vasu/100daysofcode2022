class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        stack = []
        util = []
        
        repeated = set()
        seen = set()
        
        for i in range(len(s)):
            if s[i] in repeated:
                continue
                
            elif s[i] in seen:
                
                while s[stack[-1]] != s[i]:
                    util.append(stack.pop(-1))
                
                stack.pop(-1)
                
                while len(util) > 0:
                    stack.append(util.pop(-1))
                    
                repeated.add(s[i])
                
            else:
                
                stack.append(i)
                seen.add(s[i])
                
        if len(stack) > 0:
            return stack[0]
        else:
            return -1