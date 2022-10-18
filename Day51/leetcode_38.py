class Solution:
    def countAndSay(self, n: int) -> str:
        
        digit = "1"
        for i in range(n-1):
            curr = ''
            prev = ['',0]
            for i in range(len(digit)):
                if len(prev[0]) == 0:
                    prev[0] = digit[i]
                    prev[1] += 1
                else:
                    if digit[i] == prev[0]:
                        prev[1] += 1
                    else:
                        curr = curr + str(prev[1]) + prev[0]
                        prev[0] = digit[i]
                        prev[1] = 1
            curr = curr + str(prev[1]) + prev[0]
            digit = curr
        return digit