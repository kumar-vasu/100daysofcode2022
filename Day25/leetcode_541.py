class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        stack = []
        res = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) == 2*k:
                res.extend(list(reversed(stack[:k])))
                res.extend(list(stack[k:]))
                stack = []
        
        if len(stack) > k:
            res.extend(list(reversed(stack[:k])))
            res.extend(list(stack[k:]))
        
        if len(stack) <= k:
            res.extend(list(reversed(stack)))
            
        #print(res)
        return "".join(res)