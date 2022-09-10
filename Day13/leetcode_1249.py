class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        N = len(s)

        open_ = 0
        remove = 0
        stack = []

        for i in range(N):
            if (s[i] == '(' ):
                open_ += 1
                stack.append(s[i])
            elif s[i] == ")":
                open_ -= 1
                if (open_ < 0):
                    open_ = 0
                    remove += 1
                    continue
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        
        length = len(stack)-1
        while open_ > 0:
            if stack[length] == "(":
                open_ -= 1
                stack.pop(length)
            length -= 1
        #print(open_, stack)
        
        return "".join(stack)
                
            