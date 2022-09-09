class Solution:
    def checkValidString(self, s: str) -> bool:
        if s[0] == ")" or s[-1] == "(":
            return False
        
        stack = []
        stars = []
        
        for i in range(len(s)):         
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if len(stack) > 0:
                    stack.pop(-1)
                elif len(stars) > 0:
                    stars.pop(-1)
                else:
                    return False
            else:
                stars.append(i)
            
        if len(stack) == 0:
            return True
        elif len(stars) < len(stack):
            return False
        else:
            for _ in range(len(stack)):
                curr = stack.pop(-1)
                if stars[-1] < curr:
                    return False
                else:
                    stars.pop(-1)
            return True